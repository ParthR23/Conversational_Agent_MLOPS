def steering_node(state):
    query = state["user_query"].lower()

    if "weather" in query or "temperature" in query:
        state["route"] = "weather"
    else:
        state["route"] = "knowledge"

    return state