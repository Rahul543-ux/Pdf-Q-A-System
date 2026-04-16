# 📄 PDF Q&A System (AI Powered)

A simple AI-powered app that allows you to upload a PDF and ask questions based on its content.

Built using:
- Streamlit (UI)
- LangChain (pipeline)
- FAISS (vector search)
- HuggingFace (embeddings)
- Groq (LLM for fast answers)

---

## 🚀 Features

- Upload any PDF
- Automatic text extraction & chunking
- Semantic search using embeddings
- Fast AI answers using Groq (LLaMA 3.1)
- Clean and simple UI

---

## 🧠 How It Works

1. PDF upload
2. Text extraction using PyPDFLoader
3. Text splitting into chunks
4. Convert chunks into embeddings
5. Store in FAISS vector database
6. Retrieve relevant chunks based on question
7. Send context + question to LLM (Groq)
8. Get final answer

---

## 📦 Requirements

Create a `requirements.txt` file.

1. streamlit 
2. langchain 
3. langchain-community 
4. langchain-huggingface 
5. langchain-text-splitters 
6. langchain-groq 
7. langchain-core 
8. huggingface-hub 
9. pypdf 
10. faiss-cpu 
11. sentence-transformers

---

## 🔑 Environment Variables

You need a Groq API Key.

### 👉 Set API key:

**For local:**
```bash
export GROQ_API_KEY="your_api_key"

```
**For Streamlit Cloud:**

-Go to Secrets

-Add:
```bash
GROQ_API_KEY = "your_api_key"

```

## ▶️ Run the App

```bash
streamlit run app.py

```

---

## ⚠️ Important Notes

HuggingFace is used only for embeddings (no API issues)
Groq is used for LLM → fast + reliable
Context is limited to avoid token overflow
Works best with small to medium PDFs

---

## 🛠️ Tech Stack

Python
Streamlit
LangChain
FAISS
HuggingFace Transformers
Groq API

---

## 📌 Future Improvements

Chat history (memory)
Multiple PDF support
Better UI
Streaming responses

---

## 👨‍💻 Author

Rahul Prasad

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---
