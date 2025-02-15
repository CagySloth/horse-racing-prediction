import os
from io import StringIO
from typing import Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def scrape_horse(
    path_url: str, base_url: str = os.getenv("BASE_URL")
) -> Optional[pd.DataFrame]:
    """
    Extracts a table from the HTML content using a CSS selector and returns a DataFrame.

    Args:
        path_url (str): The relative URL path to the specific webpage containing the table.
        base_url (str): The base URL of the website. Defaults to os.getenv("BASE_URL").

    Returns:
        Optional[pd.DataFrame]: df if fetching was successful, None if not.
    """
    try:
        full_url = f"{base_url}{path_url}"
        response = requests.get(full_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        selector = "#innerContent > div.commContent > div > table > tbody > tr"
        selector = (
            "#innerContent > div.commContent > div:nth-child(1) > table.horseProfile"
        )
        table = soup.select_one(selector)

        if table is None:
            return

        html_str = str(table)
        df = pd.read_html(StringIO(html_str))[0]

        return df
    except Exception as e:
        print(f"An error occurred: {e}")
