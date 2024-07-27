import os
import re

import pandas as pd

from loaders.operations import append_row_to_csv


def append_race_res(path_url: str, output_file: os.PathLike = "results/final.csv"):
    def get_bg_info(path_url: str) -> pd.DataFrame:
        bg_path_url = path_url.replace(".csv", "_bg.csv")
        df = pd.read_csv(bg_path_url, header=None)

        # Extract distance
        distance_pattern = re.compile(r"(\d+)米")
        distance_match = distance_pattern.search(df.iat[2, 0])
        distance = int(distance_match.group(1)) if distance_match else 1200
        # Extract course state
        course_state = df.iat[2, 2] or "NA"
        # Extract course
        course = df.iat[3, 2] or "NA"

        return pd.DataFrame(
            {
                "Distance": [distance],
                "CourseState": [course_state],
                "Course": [course],
            }
        )


    # read the race horses info
    df = pd.read_csv(path_url, header=None)
    # append headers to df
    headers = [
        "ID", "HorseNumber", "HorseName", "Jockey", "Position", "Trainer", "ActualWeight", 
        "BodyWeight", "Draw", "DistanceToWinner", "RunningPositions", "FinishTime", "WinOdds", "HorseUrl"
    ]
    df.columns = headers
    # Drop the 'RunningPositions' column for readability
    df = df.drop(columns=['RunningPositions'])


    bg_row = get_bg_info(path_url=path_url)
    bg_rows = pd.concat([bg_row] * len(df), ignore_index=True)

    result: pd.DataFrame = pd.concat([df.reset_index(drop=True), bg_rows.reset_index(drop=True)], axis=1)

    append_row_to_csv(output_file, result)