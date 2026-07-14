from agents.reasoning_agent import ReasoningAgent
from agents.research_agent import ResearchAgent
from graph.state import ResearchState
import re

reasoning_agent = ReasoningAgent()
research_agent = ResearchAgent()


def planner_node(state: ResearchState) -> ResearchState:
    question = state["question"]
    selected_tool = reasoning_agent.choose_tool(question)
    max_results = extract_max_results(question)

    print(f"\nPlanner selected: {selected_tool}")
    print(f"Maximum results: {max_results}\n")

    return {
        "selected_tool": selected_tool,
        "max_results": max_results,
    }

def calculator_node(state: ResearchState) -> ResearchState:
    """
    Answer a mathematical question using the calculator workflow.
    """
    answer = research_agent._answer_with_calculator(state["question"])

    return {
        "final_answer": answer,
    }


def document_search_node(state: ResearchState) -> ResearchState:
    """
    Answer using the local document-search workflow.
    """
    answer = research_agent._answer_with_document_search(state["question"])

    return {
        "final_answer": answer,
    }


def web_search_node(state: ResearchState) -> ResearchState:
    """
    Answer using current web-search results.
    """
    answer = research_agent._answer_with_web_search(state["question"])

    return {
        "final_answer": answer,
    }


def pubmed_node(state: ResearchState) -> ResearchState:
    question = state["question"]
    max_results = state.get("max_results", 10)

    answer = research_agent._answer_with_pubmed_search(
        question,
        max_results=max_results,
    )

    return {
        "final_answer": answer,
    }


def literature_review_node(state: ResearchState) -> ResearchState:
    question = state["question"]
    max_results = state.get("max_results", 10)

    answer = research_agent._answer_with_literature_review(
        question,
        max_results=max_results,
    )

    return {
        "final_answer": answer,
    }


def general_llm_node(state: ResearchState) -> ResearchState:
    """
    Answer a general question without retrieval.
    """
    answer = research_agent._answer_with_general_llm(state["question"])

    return {
        "final_answer": answer,
    }

def extract_max_results(question: str, default: int = 10) -> int:
    """
    Extract the number of requested papers from the user's question.

    Examples:
    - "Find 20 papers about Alzheimer's disease" -> 20
    - "Find recent PubMed papers" -> 10
    """

    match = re.search(r"\b(\d+)\b", question)

    if not match:
        return default

    requested_number = int(match.group(1))

    return max(1, min(requested_number, 50))