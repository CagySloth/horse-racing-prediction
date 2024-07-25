import os
import platform
import re
from typing import Tuple

import pandas as pd

# Platform-specific imports
if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl


def append_row_to_csv(file_path, row):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()

    new_row_df = pd.DataFrame([row])
    df = pd.concat([df, new_row_df], ignore_index=True)

    with open(file_path, mode="w", newline="") as file:
        if platform.system() == "Windows":
            msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, os.path.getsize(file_path))
            df.to_csv(file, index=False)
            file.flush()
            msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, os.path.getsize(file_path))
        else:
            # for unix systems
            fcntl.flock(file, fcntl.LOCK_EX)
            df.to_csv(file, index=False)
            file.flush()
            fcntl.flock(file, fcntl.LOCK_UN)


def flatten_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.unstack().reset_index(drop=True).to_frame().T


def extract_horse_values(csv_text) -> Tuple[int, int]:
    prize_money_pattern = r"總獎金\*,:,\"\$([\d,]+)\""
    rating_pattern = r"最後評分,:,(\d+)"

    # Find prize money
    prize_money_match = re.search(prize_money_pattern, csv_text)
    if prize_money_match:
        prize_money = int(prize_money_match.group(1).replace(",", ""))
    else:
        prize_money = 0

    # Find rating
    rating_match = re.search(rating_pattern, csv_text)
    if rating_match:
        rating = int(rating_match.group(1))
    else:
        rating = 50

    return prize_money, rating
