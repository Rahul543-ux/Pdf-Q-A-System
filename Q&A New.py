import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

api_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

st.set_page_config(page_title="PDF Q&A System", layout="wide")
st.title("📄 PDF Q&A System")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()

    st.success("✅ PDF processed and indexed!")

    query = st.text_input("Ask a question about your PDF")

    if query:
        if not api_key:
            st.error("Hugging Face Token not found!")
        else:
            with st.spinner("Generating answer..."):
                llm = HuggingFaceHub(
                    repo_id="google/flan-t5-base",
                    huggingfacehub_api_token=api_key,
                    model_kwargs={"temperature": 0.3, "max_length": 512}
                )

                prompt = PromptTemplate.from_template(
                    "Answer the question based on the context below.\nContext: {context}\nQuestion: {question}\nAnswer:"
                )

                chain = (
                    {"context": retriever, "question": RunnablePassthrough()}
                    | prompt
                    | llm
                    | StrOutputParser()
                )

                result = chain.invoke(query)
                st.write("### Answer:")
                st.write(result)
