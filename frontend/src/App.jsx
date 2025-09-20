// App.jsx
import React, { useState } from "react";
import axios from "axios";
import Header from "./components/Header";
import SearchForm from "./components/SearchForm";
import ResultCard from "./components/ResultCard";
import "./App.css"; // new global styles if needed

export default function App() {
  const [url, setUrl] = useState("");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    if (!url.trim() || !query.trim()) {
      setError("Please provide both URL and search query.");
      return;
    }

    setLoading(true);
    setResults([]);

    try {
      const resp = await axios.post("http://localhost:8000/api/search/", {
        url: url.trim(),
        query: query.trim(),
      });
      setResults(Array.isArray(resp.data.results) ? resp.data.results.slice(0, 10) : []);
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Check backend server.");
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setUrl("");
    setQuery("");
    setResults([]);
    setError(null);
  };

  return (
    <div className="app-container">
      <Header />
      <SearchForm
        url={url}
        query={query}
        setUrl={setUrl}
        setQuery={setQuery}
        onSubmit={handleSubmit}
        onReset={handleReset}
        loading={loading}
        error={error}
      />

      <section className="results-grid">
        {results.map((r, idx) => (
          <ResultCard key={r.id ?? idx} r={r} idx={idx} />
        ))}
      </section>
    </div>
  );
}
