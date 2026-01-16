class KnowledgeAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        
    def run(self, query: str) -> str:
        docs = self.retriever.retrieve(query)
        return f"Based on document: {docs[0]}"
    