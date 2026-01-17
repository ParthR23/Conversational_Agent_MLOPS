from zenml import step

@step
def ingest_docs() -> list[str]:
    return [
        "Retriveal-Augumented Generation combines search with LLMs."
        "Langgrpah is used for agent orchestration."
    ]