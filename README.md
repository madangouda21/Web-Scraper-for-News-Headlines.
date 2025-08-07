# 📰 News Headline Scraper

This is a simple, modular web scraper built in Python to extract headlines from a news website. The project is structured to separate concerns: fetching data, parsing data, and running the main logic.

## 🚀 Getting Started

### Prerequisites

You need Python 3 installed on your system.

### Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/your-username/news-scraper.git](https://github.com/your-username/news-scraper.git)
    cd news-scraper
    ```
2.  Install the required Python libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  Open `scraper.py` and modify the `TARGET_URL` variable to the news website you want to scrape.
2.  Run the script from your terminal:
    ```bash
    python scraper.py
    ```

The script will fetch the headlines and save them to a file named `headlines.txt` in the same directory.

## 📁 Project Structure

-   **`scraper.py`**: The entry point of the application. It orchestrates the entire scraping workflow.
-   **`fetcher.py`**: A module responsible for making HTTP requests to fetch the raw HTML content of a webpage.
-   **`parser.py`**: A module that contains the logic for parsing the HTML using `BeautifulSoup` to find headlines.
-   **`headlines.txt`**: The output file where the scraped headlines are saved.
-   **`requirements.txt`**: A list of Python libraries required for the project.
-   **`README.md`**: This file, providing an overview and instructions.

## 🛠️ Customization

To adapt this scraper for a different website, you may need to:
-   Change the `TARGET_URL` in `scraper.py`.
-   Inspect the new website's HTML structure to identify the correct tags or CSS selectors for headlines and modify the `parse_headlines` function in `parser.py` accordingly.