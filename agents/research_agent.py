from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME
from agents.reasoning_agent import ReasoningAgent
from tools.calculator import calculate
from tools.document_search import search_documents
from tools.web_search_tool import web_search
from tools.pubmed_search import search_pubmed
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

        tool_registry = {
            Tool.CALCULATOR.value: self._answer_with_calculator,
            Tool.DOCUMENT_SEARCH.value: self._answer_with_document_search,
            Tool.WEB_SEARCH.value: self._answer_with_web_search,
            Tool.PUBMED_SEARCH.value: self._answer_with_pubmed_search,
            Tool.LITERATURE_REVIEW.value: self._answer_with_literature_review,
        }

        tool_handler = tool_registry.get(selected_tool)

        if tool_handler:
            return tool_handler(question)

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

    def _answer_with_web_search(self, question: str) -> str:
        context = web_search(question)

        print("\n========== WEB SEARCH ==========")
        print(context)
        print("================================\n")

        final_prompt = f"""
Use the web search results below to answer the user's question.

User question:
{question}

Web search results:
{context}

If the search results are insufficient, say that you could not find enough information.
Answer naturally and concisely.
"""

        final_response = self.client.responses.create(
            model=self.model,
            input=final_prompt,
        )

        return final_response.output_text

    def _answer_with_pubmed_search(self, question: str) -> str:
        pubmed_query_prompt = f"""
Convert this user question into a concise PubMed search query.

User question:
{question}

Return only the PubMed search query. No explanation.
"""

        query_response = self.client.responses.create(
            model=self.model,
            input=pubmed_query_prompt,
        )

        pubmed_query = query_response.output_text.strip()

        context = search_pubmed(pubmed_query, max_results=10)

        print("\n========== PUBMED SEARCH ==========")
        print(context)
        print("===================================\n")

        final_prompt = f"""
You are a biomedical AI research assistant.

Use the PubMed article results below to answer the user's question.

User question:
{question}

PubMed results:
{context}

Write a research-focused synthesis with:
1. A brief overview of what the papers are about
2. Main methodological themes
3. Common datasets or modalities, if mentioned
4. Key limitations or open challenges
5. A short concluding takeaway

Keep the answer under 700 words.
Do not invent citations beyond the PubMed results.
Mention PMIDs when referring to specific papers.
"""

        final_response = self.client.responses.create(
            model=self.model,
            input=final_prompt,
        )

        return final_response.output_text
    
    def _answer_with_literature_review(self, question: str) -> str:
        pubmed_query_prompt = f"""
Convert this user request into a concise PubMed search query.

User request:
{question}

Return only the PubMed search query. No explanation.
"""

        query_response = self.client.responses.create(
            model=self.model,
            input=pubmed_query_prompt,
        )

        pubmed_query = query_response.output_text.strip()
        context = search_pubmed(pubmed_query, max_results=10)

        print("\n========== LITERATURE REVIEW PUBMED SEARCH ==========")
        print(f"PubMed query: {pubmed_query}")
        print(context)
        print("=====================================================\n")

        final_prompt = f"""
You are a biomedical AI research assistant.

Using the PubMed results below, write a structured mini literature review.

User request:
{question}

PubMed results:
{context}

Format the review with these sections:

# Literature Review

## Introduction

## Recent Advances

## Common Methods and Models

## Datasets and Modalities

## Limitations and Open Challenges

## Future Directions

## References

Use PMIDs in the References section.
Do not invent papers or citations beyond the PubMed results.
Keep the review concise but professional.
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