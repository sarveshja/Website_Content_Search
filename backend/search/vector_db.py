import chromadb
from sentence_transformers import SentenceTransformer
from django.conf import settings

# Initialize Chroma client (persistent storage under BASE_DIR/chroma_data)
chroma_client = chromadb.PersistentClient(path=str(settings.BASE_DIR / "chroma_data"))

# Embedding model (384-dim by default for all-MiniLM-L6-v2)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION_NAME = "html_chunks"

# Get or create a collection for HTML chunks
collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}  # cosine similarity for nearest neighbour
)

# Return embeddings for a list of texts using the sentence transformer model
def embed_text(texts):
    return embedder.encode(texts, convert_to_numpy=True).tolist()

# Insert a list of text chunks into Chroma with their embeddings and metadata
def insert_chunks(chunks, url):
    vectors = embed_text(chunks)
    ids = [f"{url}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": url} for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=metadatas,
        embeddings=vectors,
    )

# Perform semantic search in Chroma for the given query and return top_k results
def semantic_search(query, top_k=10):
    q_vec = embed_text([query])[0]

    results = collection.query(
        query_embeddings=[q_vec],
        n_results=top_k
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results.get("distances", [[None]])[0]

    # Convert cosine distance -> similarity (1 - distance)
    sims = [1.0 - d if d is not None else None for d in distances]

    combined = [
        {"chunk": doc, "source": meta.get("source"), "score": sim}
        for doc, meta, sim in zip(docs, metas, sims)
    ]

    # Sort descending by similarity score
    combined.sort(key=lambda x: x["score"], reverse=True)

    return combined
