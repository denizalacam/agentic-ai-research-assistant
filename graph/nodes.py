from agents.reasoning_agent import ReasoningAgent
from graph.state import ResearchState


reasoning_agent = ReasoningAgent()


def planner_node(state: ResearchState) -> ResearchState:
    """
    Decide which tool should handle the user's question.
    """

    question = state["question"]
    selected_tool = reasoning_agent.choose_tool(question)

    print(f"\nPlanner selected: {selected_tool}\n")

    return {
        "selected_tool": selected_tool,
    }

from agents.research_agent import ResearchAgent

research_agent = ResearchAgent()


def pubmed_node(state: ResearchState) -> ResearchState:
    """
    Execute the PubMed search workflow.
    """

    question = state["question"]

    answer = research_agent._answer_with_pubmed_search(question)

    return {
        "final_answer": answer
    }