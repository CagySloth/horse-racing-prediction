import os
from io import StringIO

import pandas as pd

from loaders.operations import append_row_to_csv, extract_horse_values
from scrapers import scrape_horse


def append_horses_info(
    path_url: str, output_file: os.PathLike = "horse_res.csv"
) -> None:
    """
    Append horse information from a given URL to a CSV file.

    This function scrapes horse information from a specified URL,
    extracts relevant values, and appends the data to a output_file csv.

    Args:
        path_url (str): The URL to scrape horse information from.
        output_file (Union[str, os.PathLike], optional):
            The path to the final horse results CSV file. Defaults to "horse_res.csv".
    """

    df: pd.DataFrame = scrape_horse(
        path_url=path_url,
        base_url="https://racing.hkjc.com/",
    )

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_text = csv_buffer.getvalue()

    prize_money, rating, gold, silver, bronze, total_matches, win_rate, birthplace = (
        extract_horse_values(csv_text=csv_text)
    )

    # Creating a DataFrame with the same columns as expected in the CSV
    new_row = pd.DataFrame(
        {
            "URL": [path_url],
            "PrizeMoney": [prize_money],
            "Rating": [rating],
            "Gold": [gold],
            "Silver": [silver],
            "Bronze": [bronze],
            "TotalMatches": [total_matches],
            "WinRate": [win_rate],
            "BirthPlace": [birthplace],
        }
    )

    append_row_to_csv(output_file, new_row)
