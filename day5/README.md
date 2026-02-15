# 🤖 AI Chatbot Platform — Day 5 Final Project

A full-stack AI chatbot built using **React**, **Node.js**, **FastAPI**, and **OpenRouter API** with an animated AI-style UI.

This project demonstrates frontend-backend integration, AI API handling, and modern UI design using an animated particle background.

---

## 🚀 Features

- 💬 Real-time AI chatbot
- ⚡ React frontend UI
- 🔧 Node.js API gateway
- 🧠 FastAPI AI backend
- 🌌 Animated particle background
- ✨ Glowing modern chatbot interface
- 🔐 API integration using OpenRouter
- 📦 Modular project structure

---

## 🧱 Tech Stack

### Frontend
- React.js
- Axios
- CSS (Custom animations)

### Backend
- Node.js + Express
- FastAPI (Python)
- Uvicorn

### AI
- OpenRouter API

---

## 📂 Project Structure

ai-chatbot/
│
├── frontend/ # React UI
│ ├── src/
│ ├── public/
│ └── package.json
│
├── backend-node/ # Node.js server (API gateway)
│ └── server.js
│
├── backend-fastapi/ # FastAPI AI backend
│ └── main.py
│
└── .gitignore



---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-ai.git
cd chatbot-ai

🖥️ FRONTEND SETUP (React)

cd frontend
npm install
npm start

🔵 NODE BACKEND SETUP

Open new terminal:

cd backend-node
npm install
node server.js


🐍 FASTAPI BACKEND SETUP

Open another terminal:

cd backend-fastapi
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn requests

Run:

uvicorn main:app --reload

```

🔑 OpenRouter API Setup

Go to: https://openrouter.ai/keys

Create API key

Open:

backend-fastapi/main.py


Replace:

API_KEY = "YOUR_API_KEY"


with your key.

▶️ Run the Full Project

You MUST run 3 terminals:

Service	Port
React Frontend	3000
Node Backend	5000
FastAPI Backend	8000
🌌 UI Highlights

Animated particle background

Neon glowing heading

Glassmorphism chatbot panel

Smooth message bubbles

🎯 Learning Outcomes (Day 5)

Full-stack architecture

API communication (React → Node → FastAPI → AI)

Async request handling

Modern chatbot UI design

Git & GitHub workflow

🚀 Future Improvements

Streaming AI responses (ChatGPT style)

Typing indicators

Chat history sidebar

Authentication

Database integration

👨‍💻 Author

Stanieio S
Cloud Enthusiast | IT Student | AI Builder
