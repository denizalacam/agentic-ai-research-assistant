from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME


class ReasoningAgent:
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
- document_search: use for questions about notes, documents, local files, RAG, tool calling, or enterprise AI
- web_search: use for recent news, current events, latest technologies, companies, or general internet information
- pubmed_search: use for biomedical papers, PubMed articles, clinical research, medical literature, neuroscience, Alzheimer's disease, cancer research, medical imaging, genomics
- general_llm: use for general explanation questions that do not require searching
- literature_review: use when the user asks to write, generate, draft, or create a literature review

User question:
{question}

Return only one of these:
calculator
document_search
web_search
pubmed_search
general_llm
literature_review
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text.strip().lower()