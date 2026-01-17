# mlops/pipelines/conversation_pipeline.py
from zenml import pipeline
from mlops.steps.load_queries import load_queries
from mlops.steps.build_rag import build_rag
from mlops.steps.run_conversations import run_conversations

@pipeline
def conversational_agent_pipeline():
    queries = load_queries()
    index_path = build_rag()
    run_conversations(queries, index_path)

if __name__ == "__main__":
    conversational_agent_pipeline()
