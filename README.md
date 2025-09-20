Website Content Search (Async Assignment)

This project is a full-stack single-page application (SPA) that allows users to input a website URL and a search query. The backend fetches and cleans the HTML from the given URL, splits the text into manageable chunks, generates embeddings using a transformer model, stores them in a vector database (ChromaDB), and performs semantic search to return the most relevant chunks.

Project Structure
```
backend
│
├── backend
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── search
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations
│ │ └── init.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ └── vector_db.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt

frontend
│
├── public
│ └── favicon.ico
│
├── src
│ ├── assets
│ │ └── styles.css
│ ├── components
│ │ ├── Header.jsx
│ │ ├── Header.module.css
│ │ ├── InputField.jsx
│ │ ├── InputField.module.css
│ │ ├── SearchForm.jsx
│ │ ├── SearchForm.module.css
│ │ ├── ResultCard.jsx
│ │ └── ResultCard.module.css
│ ├── App.jsx
│ ├── main.jsx
│ └── index.css
│
├── package.json
├── vite.config.js
└── node_modules
```
Tech Stack

Frontend uses React with Vite, Axios for API requests, and custom CSS for styling.
Backend uses Django with Django REST Framework, ChromaDB for vector storage, Sentence-Transformers for embeddings, NLTK for tokenization, BeautifulSoup and Requests for HTML fetching and parsing.

Prerequisites
```
Python version 3.10 or higher.
Node.js version 18 or higher.
Git for cloning the repository.
Virtualenv recommended for backend.
```
Backend Setup (Django)
```
Clone the repository:
git clone <repo-url>
cd backend
```
Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment:
```
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Apply migrations:
```
python manage.py migrate
```

Run the backend server:
```
python manage.py runserver
```

The backend will now be available at http://localhost:8000

Frontend Setup (React + Vite)

Navigate to the frontend folder:
```
cd frontend
```

Install dependencies:
```
npm install
```

Start the development server:
```
npm run dev
```

The frontend will now be available at http://localhost:5173

Vector Database

This project uses ChromaDB with persistent local storage.
The vector data is stored inside a folder named chroma_data located under the backend directory.
No external database installation or setup is required.

Usage

Open the frontend in your browser at http://localhost:5173

Enter a website URL and a search query.

Click the search button.

The application will display the top ten most relevant content chunks extracted from the website, along with similarity scores and source URLs.

Notes
```
The embedding model used is all-MiniLM-L6-v2 with a 384-dimensional vector space.
Cosine similarity is used for semantic matching.
Each chunk is limited to 500 words.
NLTK punkt is handled automatically in the backend at runtime and does not require manual installation.
```
Dependencies
```
Backend

Django
Django REST Framework
Django CORS Headers
Requests
BeautifulSoup4
NLTK
Sentence-Transformers
Torch
ChromaDB
TF-Keras (for compatibility with Transformers)

Frontend

React
React DOM
Vite
Axios
```
