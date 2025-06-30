import os
from langchain.document_loaders import PyPDFLoader, TextLoader, UnstructuredFileLoader


def load_documents(uploaded_files):
    documents = []
    for file in uploaded_files:
        file_name = file.name
        if file_name.endswith(".pdf"):
            loader = PyPDFLoader(file)
        elif file_name.endswith(".txt"):
            loader = TextLoader(file)
       elif file_name.endswith(".docx"):
    loader = UnstructuredFileLoader(file)

        else:
            continue
        documents.extend(loader.load())
    return documents
