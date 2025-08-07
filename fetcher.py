import requests
from requests.exceptions import RequestException

def fetch_html(url):
    """
    Fetches the HTML content from a given URL using the requests library.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The raw HTML content of the page if the request is successful.
             Returns None if there is an error.
    """
    # A custom user-agent can sometimes help avoid being blocked by a server
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # We use a timeout to prevent the script from hanging indefinitely
        response = requests.get(url, headers=headers, timeout=10)
        # Check if the request was successful
        response.raise_for_status()
        return response.text
    except RequestException as e:
        print(f"❌ An error occurred while fetching the URL: {e}")
        return None