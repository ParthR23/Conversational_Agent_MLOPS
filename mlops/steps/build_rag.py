from zenml import step
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

@step
def build_rag(documents) -> str:
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    index_path = "artifacts/faiss_index"
    os.makedirs(index_path, exist_ok=True)

    vectorstore.save_local(index_path)

    return index_path
