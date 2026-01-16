from zenml import pipeline
from mlops.steps.ingest_knowledge import ingest_knowledge
from mlops.steps.build_rag import build_rag
from mlops.steps.run_conversations import run_conversations
from mlops.steps.evaluate_agent import evaluate_agent
from mlops.steps.promote_agent import promote_agent

@pipeline
def conversational_agent_pipeline():
    documents = ingest_knowledge()
    index_path = build_rag(documents)
    results = run_conversations(index_path)


if __name__ == "__main__":
    conversational_agent_pipeline()
