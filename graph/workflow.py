from langgraph.graph import END, START, StateGraph

from graph.nodes import (
    calculator_node,
    document_search_node,
    general_llm_node,
    literature_review_node,
    planner_node,
    pubmed_node,
    web_search_node,
)
from graph.state import ResearchState


def route_after_planner(state: ResearchState) -> str:
    """
    Route the workflow according to the planner's selected tool.
    """
    selected_tool = state.get("selected_tool", "general_llm")

    route_map = {
        "calculator": "calculator",
        "document_search": "document_search",
        "web_search": "web_search",
        "pubmed_search": "pubmed",
        "literature_review": "literature_review",
        "general_llm": "general_llm",
    }

    return route_map.get(selected_tool, "general_llm")


def build_graph():
    workflow = StateGraph(ResearchState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("calculator", calculator_node)
    workflow.add_node("document_search", document_search_node)
    workflow.add_node("web_search", web_search_node)
    workflow.add_node("pubmed", pubmed_node)
    workflow.add_node("literature_review", literature_review_node)
    workflow.add_node("general_llm", general_llm_node)

    workflow.add_edge(START, "planner")

    workflow.add_conditional_edges(
        "planner",
        route_after_planner,
        {
            "calculator": "calculator",
            "document_search": "document_search",
            "web_search": "web_search",
            "pubmed": "pubmed",
            "literature_review": "literature_review",
            "general_llm": "general_llm",
        },
    )

    workflow.add_edge("calculator", END)
    workflow.add_edge("document_search", END)
    workflow.add_edge("web_search", END)
    workflow.add_edge("pubmed", END)
    workflow.add_edge("literature_review", END)
    workflow.add_edge("general_llm", END)

    return workflow.compile()