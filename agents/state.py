from typing import TypedDict, List

class AgentState(TypedDict):
    user_query: str
    route: str
    response: str
    retreived_docs: List[str]
