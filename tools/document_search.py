from pathlib import Path
import re

DOCUMENTS_DIR = Path("documents")


def normalize(text: str) -> list[str]:
    """
    Convert text to lowercase words and remove punctuation.
    """
    return re.findall(r"\b\w+\b", text.lower())


def search_documents(query: str) -> str:
    """
    Search local text documents and return relevant paragraphs.
    """
    results = []
    query_words = set(normalize(query))

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        # Split document into paragraph-like chunks
        chunks = text.split("\n\n")

        for chunk in chunks:
            chunk_words = set(normalize(chunk))
            overlap = query_words.intersection(chunk_words)

            if overlap:
                results.append(
                    f"Source: {file_path.name}\nRelevant text: {chunk.strip()}"
                )

    if not results:
        return "No relevant document passages found."

    return "\n\n".join(results[:5])