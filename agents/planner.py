from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME


class PlannerAgent:
    """
    Decides which tool the assistant should use.
    """

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL_NAME

    def choose_tool(self, question: str) -> str:
        prompt = f"""
You are a planner for an agentic AI research assistant.

Choose exactly one tool for the user's question.

Available tools:
- calculator: use for math, percentages, arithmetic, formulas
- document_search: use for questions about notes, documents, files, RAG, tool calling, enterprise AI
- general_llm: use for general explanation questions

User question:
{question}

Return only one of these:
calculator
document_search
general_llm
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text.strip().lower()