import os
import re
from typing import Tuple

import pandas as pd


def append_row_to_csv(file_path: os.PathLike, row: pd.DataFrame) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()

    df = pd.concat([df, row], ignore_index=True)

    df.to_csv(file_path, index=False)


def extract_horse_values(csv_text) -> Tuple[int | float | str]:
    prize_money_pattern = r"總獎金\*,:,\"\$([\d,]+)\""
    frating_pattern = r"最後評分,:,(\d+)"
    crating_pattern = r"現時評分,:,(\d+)"
    wins_pattern = r"冠-亞-季-總出賽次數\*,:,(\d+)-(\d+)-(\d+)-(\d+)"
    birth_pattern = r"出生地,:,([^\n]+)|出生地 / 馬齡,:,([^\s/]+)"

    # Find prize money
    prize_money_match = re.search(prize_money_pattern, csv_text)
    if prize_money_match:
        prize_money = int(prize_money_match.group(1).replace(",", ""))
    else:
        prize_money = 0

    # Find rating
    rating_match = re.search(frating_pattern, csv_text)
    if rating_match:
        rating = int(rating_match.group(1))
    else:
        rating_match = re.search(crating_pattern, csv_text)
        if rating_match:
            rating = int(rating_match.group(1))
        else:
            rating = 50

    # Find wins
    wins_match = re.search(wins_pattern, csv_text)
    if wins_match:
        gold, silver, bronze, overall_matches = map(int, wins_match.groups())
    else:
        gold, silver, bronze, overall_matches = (0, 0, 0, 0)

    # Find birthplace
    birthplace_match = re.search(birth_pattern, csv_text)
    if birthplace_match:
        birthplace = (
            birthplace_match.group(1)
            if birthplace_match.group(1)
            else birthplace_match.group(2)
        )
    else:
        birthplace = ""

    # Calculate Top 3 %
    win_rate = (gold + silver + bronze) / overall_matches

    return (
        prize_money,
        rating,
        gold,
        silver,
        bronze,
        overall_matches,
        win_rate,
        birthplace,
    )
