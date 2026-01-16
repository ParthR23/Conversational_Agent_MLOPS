def compute_metrics(results: list) -> dict:
    correct = 0

    for r in results:
        if r["predicted_route"] == r["expected_route"]:
            correct += 1
    
    routing_accuracy = correct / len(results)
    
    return{
        "routing_accuracy": routing_accuracy,
        "total_queries": len(results)
    }