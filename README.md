👩‍💻 Developed by: Vidyashree K J

📘 Overview
This project implements a Retrieval-Augmented Generation (RAG) style search system that allows users to search applicant profiles using natural language queries.

It simulates intelligent search using FAISS (vector similarity search) and FastAPI, without needing any paid API keys like OpenAI or Gemini.

⚙️ Tech Stack
Component	Technology Used
Frontend	React.js
Backend	FastAPI
Vector Search Engine	FAISS
Programming Languages	Python, JavaScript
Environment	VS Code, Node.js, Uvicorn

🚀 Features
✅ Real-time search of applicant profiles
✅ RAG-style similarity-based matching
✅ No external API key required
✅ Fully functional backend + frontend integration
✅ Simple, lightweight, and easy to extend

🏗️ Project Structure
rag_demo/
│
├── backend/
│   ├── main.py                # FastAPI backend (FAISS-based RAG logic)
│   ├── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.js             # Root React component
│   │   ├── RagSearch.jsx      # Search UI component
│   ├── package.json           # Frontend dependencies
│
└── README.md
⚡ Setup Instructions
1️⃣ Backend Setup (FastAPI)
cd backend
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
The backend will start on:
http://127.0.0.1:8000

2️⃣ Frontend Setup (React)
cd frontend
npm install
npm start
The frontend will start on:
http://localhost:3000

Make sure both backend and frontend are running simultaneously.
🔍 How It Works
The user types a query (e.g., “Python developer with React skills”).

The backend converts the text into a fake embedding (using NumPy).

FAISS finds the closest matching profiles.

The results and a short summary are sent back to the frontend.

The frontend displays them beautifully.

🧩 Example Queries
“Frontend Developer React”

“Python Django API”

“Data Scientist SQL”

“AWS Docker Engineer”

📦 Future Enhancements
Connect to Supabase or Odoo applicants database

Add semantic embeddings (OpenAI or Gemini)

Enable pagination and filters

Deploy to Render / Vercel

📚 References
FastAPI Documentation

FAISS Library

React Docs

🔗 GitHub Repository
https://github.com/<your-username>/rag-search-demo
