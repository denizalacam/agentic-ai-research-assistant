import requests
import xml.etree.ElementTree as ET


ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def search_pubmed(query: str, max_results: int = 5) -> str:
    """
    Search PubMed and return formatted paper information.

    Step 1: Use ESearch to find PubMed IDs.
    Step 2: Use EFetch to retrieve article metadata and abstracts.
    """

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "sort": "pub date",
    }

    search_response = requests.get(ESEARCH_URL, params=search_params)
    search_response.raise_for_status()

    search_data = search_response.json()
    pmids = search_data["esearchresult"]["idlist"]

    if not pmids:
        return "No PubMed articles found."

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    }

    fetch_response = requests.get(EFETCH_URL, params=fetch_params)
    fetch_response.raise_for_status()

    root = ET.fromstring(fetch_response.text)

    results_text = ""

    for i, article in enumerate(root.findall(".//PubmedArticle"), start=1):
        title = article.findtext(".//ArticleTitle", default="No title available")

        journal = article.findtext(".//Journal/Title", default="No journal available")

        year = article.findtext(".//PubDate/Year", default="No year available")

        abstract_parts = article.findall(".//Abstract/AbstractText")
        abstract = " ".join(
            part.text for part in abstract_parts if part.text
        )

        if not abstract:
            abstract = "No abstract available."

        pmid = article.findtext(".//PMID", default="No PMID available")

        results_text += f"\nPaper {i}\n"
        results_text += f"Title: {title}\n"
        results_text += f"Journal: {journal}\n"
        results_text += f"Year: {year}\n"
        results_text += f"PMID: {pmid}\n"
        results_text += f"Abstract: {abstract}\n"
        results_text += "-" * 60 + "\n"

    return results_text