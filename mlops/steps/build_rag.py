from zenml import step
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import os

@step
def build_rag() -> str:
    docs = [
        Document(page_content="RAG combines retrieval with generation"),
        Document(page_content="FAISS is a vector similarity search library")
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    index_path = "artifacts/faiss_index"
    os.makedirs(index_path, exist_ok=True)

    vectorstore.save_local(index_path)

    return index_path
