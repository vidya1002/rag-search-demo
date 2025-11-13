import React, { useState } from "react";

export default function RagSearch() {
    const [query, setQuery] = useState("");
    const [answer, setAnswer] = useState("");
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);

    async function handleSearch(e) {
        e.preventDefault();
        setLoading(true);
        setAnswer("");
        setResults([]);

        try {
            const res = await fetch("http://127.0.0.1:8000/search", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query }),
            });

            if (!res.ok) throw new Error("Server error");

            const data = await res.json();
            setAnswer(data.answer);
            setResults(data.results);
        } catch (err) {
            setAnswer("⚠️ Unable to connect to backend. Please check if it's running.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <div style={{ maxWidth: "700px", margin: "auto", padding: "20px" }}>
            <h2>Applicant RAG Search (No API Keys)</h2>
            <form onSubmit={handleSearch}>
                <input
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search for a role or skill..."
                    style={{ width: "75%", padding: "8px" }}
                />
                <button type="submit" style={{ padding: "8px 12px" }}>
                    {loading ? "Searching..." : "Search"}
                </button>
            </form>

            <h3 style={{ marginTop: "20px" }}>Answer:</h3>
            <pre>{answer}</pre>

            <h3>Matching Profiles:</h3>
            {results.map((r) => (
                <div
                    key={r.id}
                    style={{
                        border: "1px solid #ddd",
                        margin: "8px 0",
                        padding: "8px",
                        borderRadius: "6px",
                    }}
                >
                    <strong>{r.name}</strong> - {r.role}
                    <br />
                    <em>{r.summary}</em>
                    <br />
                    <small>
                        Skills: {Array.isArray(r.skills) ? r.skills.join(", ") : r.skills}
                    </small>
                </div>
            ))}
        </div>
    );
}
