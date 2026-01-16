from zenml import step
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from agents.steering_agent import SteeringAgent
from agents.knowledge_agent import KnowledgeAgent
from evaluation.conversations import conversations

@step
def run_conversations(index_path: str):
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    steering = SteeringAgent()
    knowledge = KnowledgeAgent(retriever)

    results = []

    # Ensure conversations() returns list of dicts
    for turn in conversations():  
        # If using dicts
        user_input = turn["user"]
        expected_route = turn["expected_route"]

        route = steering.route(user_input)

        if route == "knowledge":
            response = knowledge.answer(user_input)
        else:
            response = "Handled by other skill"

        results.append({
            "query": user_input,
            "predicted_route": route,
            "response": response,
            "expected_route": expected_route
        })

    return results

