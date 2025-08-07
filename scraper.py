import os
import sys

# It's good practice to ensure the script's directory is in the Python path
# to handle imports correctly, especially in more complex projects.
sys.path.append(os.path.dirname(__file__))

from fetcher import fetch_html
from parser import parse_headlines

def save_headlines_to_file(headlines, filename="headlines.txt"):
    """
    Saves a list of headlines to a text file.

    Args:
        headlines (list): A list of strings, where each string is a headline.
        filename (str): The name of the file to save the headlines to.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(f"{headline}\n")
        print(f"✅ Successfully saved {len(headlines)} headlines to '{filename}'.")
    except IOError as e:
        print(f"❌ Error saving headlines to file: {e}")

def main():
    """
    The main function to run the web scraper.
    """
    # Define the target URL for scraping. You can change this to any news site.
    TARGET_URL = "https://www.bbc.com/news"
    OUTPUT_FILE = "headlines.txt"

    print("--- 📰 News Headline Scraper ---")
    print(f"Attempting to scrape headlines from: {TARGET_URL}")

    # Step 1: Fetch the HTML content
    html_content = fetch_html(TARGET_URL)

    if html_content:
        # Step 2: Parse the HTML to extract headlines
        print("Parsing HTML content to find headlines...")
        headlines_list = parse_headlines(html_content)

        if headlines_list:
            print(f"Found {len(headlines_list)} potential headlines.")
            # Step 3: Save the headlines to a file
            save_headlines_to_file(headlines_list, OUTPUT_FILE)
        else:
            print("No headlines were found on the page.")
    else:
        print("Scraping process aborted due to an error fetching the URL.")

if __name__ == "__main__":
    main()