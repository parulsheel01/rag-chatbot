# RAG Chatbot using LM Studio, FAISS and Streamlit

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using:

- Streamlit (Frontend)
- LM Studio (Local LLM Inference)
- FAISS (Vector Database)
- Sentence Transformers (Embeddings)
- PyPDF (PDF Processing)

The chatbot allows users to ask questions about a PDF document. Instead of sending the entire document to the LLM, the system retrieves the most relevant chunks and provides them as context to generate accurate responses.

---

## Features

- PDF document ingestion
- Text chunking
- Embedding generation
- Vector similarity search using FAISS
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using LM Studio
- Real-time streaming responses
- Source chunk display

---

## Tech Stack

Python — Core application development
Streamlit — Interactive web interface
LM Studio — Local LLM serving and inference
Mistral 7B — Large Language Model for response generation
Sentence Transformers — Semantic embedding generation
FAISS — High-performance vector similarity search
PyPDF — PDF text extraction and processing
NumPy — Numerical computations and vector operations
LangChain Text Splitters — Intelligent document chunking

---

## Project Structure

```text
rag-chatbot/
│
├── data/
│   └── AI Training Document.pdf
│
├── chunks/
│   └── chunks.json
│
├── vectordb/
│   └── faiss.index
│
├── src/
│   ├── chunking.py
│   ├── embedding.py
│   ├── retriever.py
│   ├── generator.py
│   └── rag_pipeline.py
│
├── build_index.py
├── app.py
├── requirements.txt
└── README.md
```