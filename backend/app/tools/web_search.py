import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Initialize summarizer (HuggingFace model)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def web_search(query: str) -> str:
    """
    Perform a DuckDuckGo search and summarize the first result.
    """
    try:
        # DuckDuckGo search
        search_url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(search_url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        # Extract first few results
        results = soup.find_all("a", {"class": "result__a"}, limit=1)
        if not results:
            return "No search results found."

        first_url = results[0]["href"]

        # Fetch first URL content
        page_res = requests.get(first_url, headers=headers, timeout=5)
        page_soup = BeautifulSoup(page_res.text, "html.parser")
        paragraphs = page_soup.find_all("p")
        text_content = " ".join([p.get_text() for p in paragraphs[:10]])  # first 10 paragraphs

        # Summarize
        summary = summarizer(text_content, max_length=130, min_length=30, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Web search failed: {e}"