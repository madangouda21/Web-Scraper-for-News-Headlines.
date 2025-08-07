from bs4 import BeautifulSoup
from typing import List

def parse_headlines(html_content: str) -> List[str]:
    """
    Parses the HTML content to extract headlines.

    This function uses BeautifulSoup to find all HTML elements that are likely
    to contain headlines, such as h1, h2, and h3 tags.

    Args:
        html_content (str): The HTML content as a string.

    Returns:
        List[str]: A list of cleaned headline strings. Returns an empty list
                   if no content is provided or no headlines are found.
    """
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = []

    # A more robust way to find headlines is to inspect the website's HTML
    # for specific classes or IDs. For a general scraper, targeting
    # common header tags is a good starting point.
    headline_tags = soup.find_all(['h1', 'h2', 'h3'])

    for tag in headline_tags:
        # .get_text(strip=True) removes leading/trailing whitespace
        text = tag.get_text(strip=True)
        # Exclude empty strings that might result from the stripping
        if text:
            headlines.append(text)

    return headlines