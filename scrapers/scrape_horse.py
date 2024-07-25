import os

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def scrape_horse(path_url: str, base_url: str = os.getenv("BASE_URL")) -> bool:
    """
    Extracts a table from the HTML content using a CSS selector and returns a DataFrame.

    Args:
        path_url (str): The relative URL path to the specific webpage containing the table.
        base_url (str): The base URL of the website. Defaults to os.getenv("BASE_URL").

    Returns:
        bool: Whether the fetching was successful.
    """
    print(base_url, path_url)
    try:
        full_url = f"{base_url}{path_url}"
        response = requests.get(full_url)
        response.raise_for_status()
        print(full_url)
        soup = BeautifulSoup(response.content, "html.parser")
        selector = "#innerContent > div.commContent > div > table > tbody > tr"
        # selector = "#innerContent > div.commContent > div:nth-child(1) > table.horseProfile"
        table = soup.select_one(selector)

        if table is None:
            return False

        df = pd.read_html(str(table))[0]
        print(df)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
