from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import faiss
import numpy as np

app = FastAPI(title="Free RAG Search (No API Keys)")

# ✅ Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Mock profile data
profiles = [
    {"id": 1, "name": "Alice", "role": "Frontend Developer", "summary": "Expert in React, Vue, and CSS frameworks.", "skills": ["React", "JavaScript", "CSS"]},
    {"id": 2, "name": "Bob", "role": "Backend Developer", "summary": "Skilled in Python, Django, and REST APIs.", "skills": ["Python", "Django", "API"]},
    {"id": 3, "name": "Charlie", "role": "Data Scientist", "summary": "Experienced with machine learning, pandas, and SQL.", "skills": ["ML", "pandas", "SQL"]},
    {"id": 4, "name": "Diana", "role": "Full Stack Engineer", "summary": "Works with Node.js, React, and PostgreSQL.", "skills": ["Node.js", "React", "PostgreSQL"]},
    {"id": 5, "name": "Eve", "role": "DevOps Engineer", "summary": "Focuses on AWS, Docker, and Kubernetes.", "skills": ["AWS", "Docker", "Kubernetes"]}
]

# 🔢 Fake embeddings
def fake_embed(text: str):
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(384).astype("float32")

# 🧩 Build FAISS index
dim = 384
index = faiss.IndexFlatL2(dim)
vectors = [fake_embed(f"{p['name']} {p['summary']} {p['skills']}") for p in profiles]
index.add(np.array(vectors))

# 🧾 Input model
class SearchBody(BaseModel):
    query: str
    top_k: int = 3

@app.post("/search")
def search_profiles(body: SearchBody):
    query_vec = fake_embed(body.query).reshape(1, -1)
    D, I = index.search(query_vec, body.top_k)
    matches = [profiles[i] for i in I[0]]

    answer = "Here are candidates that match your query:\n"
    for p in matches:
        answer += f"- {p['name']} ({p['role']}) — skills: {', '.join(p['skills'])}\n"

    return {"query": body.query, "answer": answer.strip(), "results": matches}

@app.get("/")
def home():
    return {"message": "RAG demo running — use POST /search with { 'query': 'python developer' }"}
