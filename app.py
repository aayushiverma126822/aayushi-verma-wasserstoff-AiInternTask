import streamlit as st
from document_loader import load_documents
from theme_identifier import create_db, answer_query

st.set_page_config(page_title="Doc Chatbot", layout="wide")
st.title("📄 AI Document Chatbot + Theme Identifier")

uploaded_files = st.file_uploader("Upload PDFs / Text / Docx", type=["pdf", "txt", "docx"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Reading documents..."):
        docs = load_documents(uploaded_files)
        db = create_db(docs)
    st.success("Documents processed and ready!")

    query = st.text_input("Ask a question based on your documents:")

    if query:
        with st.spinner("Thinking..."):
            response = answer_query(db, query)
        st.write("### Answer")
        st.write(response)
