from zenml import step
from langchain_core.documents import Document


@step
def ingest_knowledge():
    raw_texts = [
        "Paris is the capital of France.",
        "London is the capital of the UK.",
        "Berlin is the capital of Germany."
    ]

    documents = [
        Document(page_content=text)
        for text in raw_texts
    ]

    return documents
