from langgraph.graph import END, START, StateGraph

from graph.nodes import planner_node, pubmed_node
from graph.state import ResearchState


def route_after_planner(state: ResearchState):
    if state["selected_tool"] == "pubmed_search":
        return "pubmed"

    return END

def build_graph():
    workflow = StateGraph(ResearchState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("pubmed", pubmed_node)
    workflow.add_conditional_edges(
    "planner",
    route_after_planner,
    {
        "pubmed": "pubmed",
        END: END,
    },
    )

    workflow.add_edge("pubmed", END)

    return workflow.compile()