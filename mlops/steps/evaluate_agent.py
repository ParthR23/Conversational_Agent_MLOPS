from zenml import step
from evaluation.metrics import compute_metrics

@step
def evaluate_agent(results: list):
    return compute_metrics(results)
    