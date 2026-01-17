# mlops/steps/load_queries.py
from zenml import step

@step
def load_queries() -> list[dict]:
    return [
        {"user": "What is RAG?"},
        {"user": "How does FAISS work?"},
        {"user": "What is the weather in London?"}
    ]
