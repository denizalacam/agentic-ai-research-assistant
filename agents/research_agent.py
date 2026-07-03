from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME
from tools.calculator import calculate
from tools.document_search import search_documents


class ResearchAgent:
    """
    A simple agent that can answer questions and use tools.
    """

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL_NAME

    def should_use_calculator(self, question: str) -> bool:
        math_keywords = ["calculate", "percent", "%", "+", "-", "*", "/", "times", "divided"]
        return any(keyword in question.lower() for keyword in math_keywords)

    def should_search_documents(self, question: str) -> bool:
        research_keywords = [
            "document",
            "notes",
            "rag",
            "retrieval",
            "agentic ai",
            "tool calling",
            "enterprise",
        ]
        return any(keyword in question.lower() for keyword in research_keywords)

    def answer(self, question: str) -> str:
        if self.should_use_calculator(question):
            expression_prompt = f"""
Extract only the mathematical expression needed to answer this question.

Question: {question}

Return only the expression. Do not explain.
"""
            expression_response = self.client.responses.create(
                model=self.model,
                input=expression_prompt,
            )

            expression = expression_response.output_text.strip()
            tool_result = calculate(expression)

            final_prompt = f"""
You are a professional AI research assistant.

The user asked:
{question}

The correct numerical result is:
{tool_result}

Respond naturally and clearly. Do not mention internal tools.
"""
            final_response = self.client.responses.create(
                model=self.model,
                input=final_prompt,
            )

            return final_response.output_text

        if self.should_search_documents(question):
            context = search_documents(question)
            print("\n========== DOCUMENT SEARCH ==========")
            print(context)
            print("====================================\n")

            final_prompt = f"""
You are a professional AI research assistant.

Answer the user's question using the document context below.

User question:
{question}

Document context:
{context}

If the context is insufficient, say that the documents do not contain enough information.
"""
            final_response = self.client.responses.create(
                model=self.model,
                input=final_prompt,
            )

            return final_response.output_text

        response = self.client.responses.create(
            model=self.model,
            input=question,
        )

        return response.output_text