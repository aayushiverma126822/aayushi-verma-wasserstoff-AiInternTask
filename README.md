# aayushi-verma-wasserstoff-AiInternTask
Document Theme Identification Chatbot for Internship Task
# 📄 Document Chatbot for Wasserstoff Internship

This project allows users to upload documents (PDF, TXT, DOCX), ask questions, and receive extracted answers and themes using LLMs.

## Features
- Upload 75+ documents
- Supports OCR
- Accurate citations (page/para)
- Synthesized themes for each query

## Stack
- Python, Streamlit, LangChain, OpenAI
- FAISS/Chroma for search
- Deployed on Vercel

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
