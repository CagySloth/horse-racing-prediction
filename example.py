from datetime import datetime, timedelta

from scrapers.list_dates import get_dates
from scrapers.scrape_race import scrape

# Calculate the start and end dates
end_date = datetime.now()
start_date = end_date - timedelta(days=1 * 365)
dates = get_dates(start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d"))

# data should look like: [{'date': '2024/06/19', 'weekday': 'weds', 'loc':'ST'}, {'date': '2024/07/06', 'weekday': 'sat', 'loc': 'HV'}...]
print(f"{dates=}")

for date in dates:
    flag = True
    i = 1
    while flag:
        flag = scrape(date["date"], date["loc"], race_no=i)
        i += 1
