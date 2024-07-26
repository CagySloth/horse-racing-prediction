import os
from io import StringIO

import pandas as pd

from loaders.operations import append_row_to_csv, extract_horse_values
from scrapers.scrape_horse import scrape_horse


def append_horses_info(path_url: str, output_file: os.PathLike = "horse_res.csv"):
    # Assuming scrape_horse and extract_horse_values are defined elsewhere
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


directory = "results/"
output_file = "results/horse_res.csv"
files = os.listdir(directory)

existing_links = set()

if os.path.exists(output_file):
    output_df = pd.read_csv(output_file)
    if len(output_df.columns) > 0:
        existing_links = set(output_df.iloc[:, 0])

for file in files:
    if file.endswith(".csv") and not file.endswith("_bg.csv"):
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)

        if len(df.columns) >= 13:
            links = df.iloc[:, 12]

            for link in links:
                if pd.notna(link):
                    if link not in existing_links:
                        print(f"Appending link: {link} to {output_file}")
                        append_horses_info(link, output_file)
                        existing_links.add(link)
                    else:
                        # print(f"Link {link} already exists in {output_file}")
                        pass
                else:
                    print("Empty")


# Read the CSV again to drop duplicates
if os.path.exists(output_file):
    df = pd.read_csv(output_file)
    df = df.drop_duplicates()
    df.to_csv(output_file, index=False)
