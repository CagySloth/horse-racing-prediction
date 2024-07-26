from scrapers.scrape_horse import scrape_horse

df = scrape_horse("racing/information/Chinese/Horse/Horse.aspx?HorseId=HK_2021_G463")

print("df:", df)
df.to_csv("temp2.csv")
