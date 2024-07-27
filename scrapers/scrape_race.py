import os
from typing import Dict, List, Literal, Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def fetch_html(race_url: str, params: Dict[str, str]) -> bytes:
    """
    Fetch the HTML content from the given race URL with parameters.

    Args:
        race_url (str): The race URL of the webpage.
        params (Dict[str, str]): The parameters to be appended to the race URL.

    Returns:
        bytes: The HTML content of the webpage.
    """
    response = requests.get(race_url, params=params)
    response.raise_for_status()
    return response.content


def extract_and_save_table(
    html_content: bytes,
    css_selector: str,
    file_path: str,
    headers: Optional[List[str]] = None,
    length_col: bool = False,
) -> Optional[pd.DataFrame]:
    """
    Extracts a table from the HTML content using a CSS selector and saves it as a CSV file.

    Args:
        html_content (bytes): The HTML content of the webpage.
        css_selector (str): The CSS selector to locate the table in the HTML.
        file_path (str): The file path where the CSV file will be saved.
        headers (Optional[List[str]]): whether headers are provided.
        length (bool): whether a col of length should be appended.
    Return:
        Optional[DataFrame]: whether the fetching was successful
    """

    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.select_one(css_selector)

    rows = []
    urls = []

    if table:
        for row in table.find_all("tr"):
            columns = row.find_all("td")
            if columns:
                row_data = [column.text.strip() for column in columns]
                rows.append(row_data)

                # Extract URL from the third column (horse column) and append it to the df
                link = columns[2].find("a", href=True)
                urls.append(link["href"] if link else None)

    df = pd.DataFrame(rows)
    if df.empty:
        return

    # append headers
    if headers:
        df.columns = headers

    # append length col if specified
    if length_col:
        df["Contenders"] = len(df)
        print("have legnth")

    df["URL"] = urls
    df.to_csv(file_path, index=False)
    return df


def scrape_race(
    race_date: str = "2019/01/23",
    racecourse: Literal["HV", "ST"] = "HV",
    race_no: str = "2",
) -> bool:
    """
    Main function to fetch HTML, extract tables, and save them as CSV files.

    Args:
        race_date (str): The date of the race in "YYYY/MM/DD" format.
        racecourse (str): The code of the racecourse.
        race_no (str): The race number.
    Return:
        bool: whether the fetching was successful
    """

    race_url: Optional[str] = os.getenv("RACE_URL")
    results_folder_url: Optional[str] = os.getenv("RESULTS_FOLDER")
    file_name: str = f"res_{race_date.replace('/', '-')}{racecourse}{race_no}"
    file_bg_name: str = f"res_{race_date.replace('/', '-')}{racecourse}_bg"

    if not (race_url and results_folder_url):
        raise ValueError("RACE_URL or RESULTS_FOLDER environment variable is not set")

    params = {"RaceDate": race_date, "Racecourse": racecourse, "RaceNo": race_no}

    html_content = fetch_html(race_url, params)

    # Race Table
    table1_selector = "#innerContent > div.localResults.commContent.fontFam > div:nth-child(5) > table > tbody"
    success1 = extract_and_save_table(
        html_content,
        table1_selector,
        os.path.join(results_folder_url, f"{file_name}.csv"),
        headers=[
            "Position",
            "HorseNumber",
            "HorseName",
            "Jockey",
            "Trainer",
            "ActWeightIncr",
            "HorseWeight",
            "GatePosition",
            "WinningMargin",
            "RunningPosition",
            "FinishTime",
            "WinOdds",
        ],
        length_col=True,
    )
    print(f"HEADERS {success1.columns}")

    # Race Background Table
    success2 = table2_selector = (
        "#innerContent > div.localResults.commContent.fontFam > div.race_tab > table"
    )
    file_path = os.path.join(results_folder_url, f"{file_bg_name}.csv")
    if not os.path.exists(file_path):
        extract_and_save_table(
            html_content,
            table2_selector,
            file_path,
        )

    if success1 is not None and success2 is not None:
        print(f"FETCHED date:{race_date}\tloc:{racecourse}\tround:{race_no}")
        return True
    else:
        print(f"FAILED date:{race_date}\tloc:{racecourse}\tround:{race_no}")
        return False
