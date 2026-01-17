from ragas import evaluate
from ragas.metrics import(
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy
)

def evaluate_rag(dataset):
    return evaluate(
        dataset,
        metrics=[
            context_precision,
            context_recall,
            faithfulness,
            answer_relevancy
        ]
    )