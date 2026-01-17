from langgraph.graph import StateGraph, END
from agents.state import AgentState
from agents.steering_agent import steering_node

def build_agent(rag_chain, weather_agent):
    graph = StateGraph(AgentState)

    graph.add_node("steering", steering_node)

    def rag_node(state):
        result = rag_chain.invoke(state["user_query"])
        state["response"] = result["result"]
        state["retrieved_docs"] = [
            d.page_content for d in result["source_documents"]
        ]
        return state

    graph.add_node("rag", rag_node)

    graph.add_node(
        "weather",
        lambda s: {
            **s,
            "response": weather_agent.run(s["user_query"])
        }
    )

    graph.set_entry_point("steering")

    graph.add_conditional_edges(
        "steering",
        lambda s: s["route"],
        {
            "knowledge": "rag",
            "weather": "weather"
        }
    )

    graph.add_edge("rag", END)
    graph.add_edge("weather", END)

    return graph.compile()
