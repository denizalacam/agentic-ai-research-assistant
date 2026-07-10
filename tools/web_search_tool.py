from ddgs import DDGS


def web_search(query: str, max_results: int = 5) -> str:
    """
    Search the web and return a formatted summary of results.

    Parameters
    ----------
    query : str
        The search query entered by the user.

    max_results : int
        Number of search results to return.

    Returns
    -------
    str
        A formatted string containing search results.
    """

    results_text = ""

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)

        for i, result in enumerate(results, start=1):
            title = result.get("title", "No title")
            url = result.get("href", "No URL")
            body = result.get("body", "No description")

            results_text += f"\nResult {i}:\n"
            results_text += f"Title: {title}\n"
            results_text += f"URL: {url}\n"
            results_text += f"Summary: {body}\n"

    if not results_text:
        return "No web search results found."

    return results_text