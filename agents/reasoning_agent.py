from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME
from agents.reasoning_agent import ReasoningAgent
from tools.calculator import calculate
from tools.document_search import search_documents
from tools.tool_types import Tool


class ResearchAgent:
    """
    Coordinates the agent workflow:
    1. Ask ReasoningAgent which tool to use.
    2. Execute the selected tool.
    3. Ask the LLM to write the final answer.
    """

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL_NAME
        self.reasoning_agent = ReasoningAgent()

    def answer(self, question: str) -> str:
        selected_tool = self.reasoning_agent.choose_tool(question)

        if selected_tool == Tool.CALCULATOR:
            return self._answer_with_calculator(question)

        if selected_tool == Tool.DOCUMENT_SEARCH:
            return self._answer_with_document_search(question)

        return self._answer_with_general_llm(question)

    def _answer_with_calculator(self, question: str) -> str:
        expression_prompt = f"""
Extract only the mathematical expression needed to answer this question.

Question:
{question}

Return only the expression.
"""

        expression_response = self.client.responses.create(
            model=self.model,
            input=expression_prompt,
        )

        expression = expression_response.output_text.strip()
        result = calculate(expression)

        final_prompt = f"""
The user asked:
{question}

The correct result is:
{result}

Answer naturally and concisely. Do not mention internal tools.
"""

        final_response = self.client.responses.create(
            model=self.model,
            input=final_prompt,
        )

        return final_response.output_text

    def _answer_with_document_search(self, question: str) -> str:
        context = search_documents(question)

        print("\n========== DOCUMENT SEARCH ==========")
        print(context)
        print("====================================\n")

        final_prompt = f"""
Use the document context below to answer the user's question.

User question:
{question}

Document context:
{context}

If the context is insufficient, say that the documents do not contain enough information.
Answer naturally and concisely.
"""

        final_response = self.client.responses.create(
            model=self.model,
            input=final_prompt,
        )

        return final_response.output_text

    def _answer_with_general_llm(self, question: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=question,
        )

        return response.output_text