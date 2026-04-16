📄 PDF Q&A System (AI Powered)
A simple AI-powered app that allows you to upload a PDF and ask questions based on its content.

Built using:

Streamlit (UI)

LangChain (Pipeline)

FAISS (Vector Search)

HuggingFace (Embeddings)

Groq (LLM for fast answers)

🚀 Features
Upload any PDF: Easily process document content.

Automatic Extraction: Text extraction & chunking done in real-time.

Semantic Search: Uses vector embeddings for precise context retrieval.

Fast AI Answers: Powered by Groq (LLaMA 3.1) for near-instant responses.

Clean UI: Simple and intuitive user interface.

🧠 How It Works
PDF Upload: User provides the document.

Extraction: Text is pulled using PyPDFLoader.

Chunking: Text is split into manageable pieces using RecursiveCharacterTextSplitter.

Embeddings: Chunks are converted into vectors via HuggingFace.

Vector Store: Vectors are indexed in a FAISS database.

Retrieval: The system finds the top 2 relevant chunks based on your question.

Generation: Context + Question are sent to Groq LLM.

Output: You get a concise, accurate answer.

📦 Requirements
Create a requirements.txt file with the following dependencies:

Plaintext
streamlit
langchain
langchain-community
langchain-huggingface
langchain-text-splitters
langchain-groq
langchain-core
huggingface-hub
pypdf
faiss-cpu
sentence-transformers
🔑 Environment Variables
You need a Groq API Key to run this application.

👉 Set API key:
For Local Development:

Bash
# Linux/Mac
export GROQ_API_KEY="your_api_key"

# Windows
set GROQ_API_KEY="your_api_key"
For Streamlit Cloud:

Go to your App Settings -> Secrets.

Add the following:

Ini, TOML
GROQ_API_KEY = "your_api_key_here"
▶️ Run the App
Bash
streamlit run app.py
⚠️ Important Notes
Embeddings: HuggingFace is used locally for embeddings, so no API key is required for this part.

Performance: Groq is used for the LLM layer, ensuring fast and reliable text generation.

Token Management: Context is optimized to avoid token overflow.

Scope: Works best with small to medium-sized PDF files.

🛠️ Tech Stack
Language: Python

Frontend: Streamlit

Framework: LangChain

Vector DB: FAISS

Models: HuggingFace Transformers & Groq API

📌 Future Improvements
[ ] Chat History: Adding memory for follow-up questions.

[ ] Multi-PDF Support: Ability to query multiple documents at once.

[ ] Enhanced UI: Custom CSS and better layout.

[ ] Streaming: Real-time word-by-word responses.

👨‍💻 Author
Rahul

⭐ If you like this project, give it a star on GitHub!
