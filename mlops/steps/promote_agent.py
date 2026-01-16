from zenml import step

@step
def promote_agent(metrics: dict):
    if metrics["routing_accuracy"] >= 0.9:
        print("Agent promoted to production")
    else:
        print("Agent failed quality gate")
        