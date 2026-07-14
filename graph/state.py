from typing import TypedDict


class ResearchState(TypedDict, total=False):
    """
    Shared state passed between LangGraph nodes.
    """

    question: str
    selected_tool: str
    max_results: int
    retrieved_context: str
    final_answer: str
    