from io import StringIO
from os import PathLike

import pandas as pd

from loaders.operations import append_row_to_csv, extract_horse_values
from scrapers.scrape_horse import scrape_horse


def consolidate_horses_info(path_url: str, output_file: PathLike = "horse_res.csv"):
    df: pd.DataFrame = scrape_horse(
        path_url=path_url,
        base_url="https://racing.hkjc.com/",
    )

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_text = csv_buffer.getvalue()

    prize_money, rating = extract_horse_values(csv_text=csv_text)
    print(f"{prize_money=} {rating=}")

    append_row_to_csv(output_file, pd.DataFrame([path_url, prize_money, rating]))


consolidate_horses_info(
    "/racing/information/Chinese/Horse/Horse.aspx?HorseId=HK_2017_B402", "horse_res.csv"
)
