class Retriever:
    def __init__(self, index):
        self.index = index
        
    def retrieve(self, query: str):
        return self.index[:1]