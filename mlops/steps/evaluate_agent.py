from zenml import step
from evaluation.ragas_eval import evaluate_rag

@step
def evaluate_agent(results: list):
    scores = evaluate_rag(results)
    return scores    