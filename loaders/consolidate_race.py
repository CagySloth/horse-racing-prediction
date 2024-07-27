import os
import re

import pandas as pd

from loaders.operations import append_row_to_csv


def append_race_res(
    path_url: str, output_file: os.PathLike = "results/final.csv"
) -> None:
    """
    Append race results from a given CSV file to another CSV file.

    This function reads race information from a specified CSV file (individual race res),
    extracts additional race background information from a related CSV file,
    and appends the combined data to a final results CSV file.

    Args:
        path_url (str): The path to the CSV file containing race results.
        output_file (Union[str, os.PathLike], optional): The path to the final results CSV file.
                                                         Defaults to "results/final.csv".
    """

    def get_bg_info(path_url: str) -> pd.DataFrame:
        """
        Extract background information about the race from a related CSV file.

        Args:
            path_url (str): The path to the race bg results.

        Returns:
            pd.DataFrame: A DataFrame containing the distance, course state, and course of the race.
        """
        bg_path_url = re.sub(r"(\d+)\.csv$", "_bg.csv", path_url)
        df = pd.read_csv(bg_path_url, header=None)

        # Extract distance
        distance_pattern = re.compile(r"(\d+)米")
        distance_match = distance_pattern.search(df.iat[3, 0])
        distance = int(distance_match.group(1)) if distance_match else 1200
        # Extract course state
        course_state = df.iat[3, 2] or "NA"
        # Extract course
        course = df.iat[4, 2] or "NA"

        return pd.DataFrame(
            {
                "Distance": [distance],
                "CourseState": [course_state],
                "Course": [course],
            }
        )

    # read the race horses info
    df = pd.read_csv(path_url)

    # Drop the 'RunningPosition' column for readability
    df = df.drop(columns=["RunningPosition"])

    bg_row = get_bg_info(path_url=path_url)
    bg_rows = pd.concat([bg_row] * len(df), ignore_index=True)

    result: pd.DataFrame = pd.concat(
        [df.reset_index(drop=True), bg_rows.reset_index(drop=True)], axis=1
    )

    append_row_to_csv(output_file, result)
