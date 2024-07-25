from scrapers.scrape_horse import scrape_horse

df = scrape_horse(
    "/racing/information/Chinese/Horse/Horse.aspx?HorseId=HK_2017_B402",
    "https://racing.hkjc.com/",
)

# df = flatten_df(df)
print(f"{df=}")

df.to_csv("horse_res.csv")
# combine.append_row_to_csv("horse.csv", row)
