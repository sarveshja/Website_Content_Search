import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .vector_db import insert_chunks, semantic_search

# Ensure punkt is available for tokenization
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Fetch and clean HTML content from a URL, removing script/style/noscript tags
def fetch_clean_html(url):
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0 Safari/537.36"
            )
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        return None, str(e)

    soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    text = soup.get_text(separator=" ")
    return text, None

# Split a string of text into chunks of max_tokens words
def chunk_text(text, max_tokens=500):
    words = word_tokenize(text)
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunk = " ".join(words[i:i + max_tokens])
        chunks.append(chunk)
    return chunks

# API endpoint: fetch HTML, chunk it, store in Chroma, perform semantic search
@api_view(["POST"])
def search_chunks(request):
    url = request.data.get("url")
    query = request.data.get("query")

    if not url or not query:
        return Response(
            {"error": "URL and query are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    text, error = fetch_clean_html(url)
    if error:
        return Response(
            {"error": f"Failed to fetch HTML: {error}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    chunks = chunk_text(text)

    if not chunks:
        return Response(
            {"error": "No valid text extracted from the given URL."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    insert_chunks(chunks, url)

    results = semantic_search(query, top_k=10)

    return Response({"results": results})
