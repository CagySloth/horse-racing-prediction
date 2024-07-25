import os
import re
from typing import Tuple

import pandas as pd

import os
import pandas as pd

def append_row_to_csv(file_path: os.PathLike, row: pd.DataFrame) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()

    df = pd.concat([df, row], ignore_index=True)

    df.to_csv(file_path, index=False)


def flatten_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.unstack().reset_index(drop=True).to_frame().T


def extract_horse_values(csv_text) -> Tuple[int, int]:
    prize_money_pattern = r"總獎金\*,:,\"\$([\d,]+)\""
    frating_pattern = r"最後評分,:,(\d+)"
    crating_pattern = r"現時評分,:,(\d+)"

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

    return prize_money, rating
