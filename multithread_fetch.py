from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

from scrapers.list_dates import get_dates
from scrapers.scrape_race import scrape_race


def scrape_race_for_date(date_info):
    date = date_info["date"]
    loc = date_info["loc"]
    i = 1
    while True:
        success = scrape_race(date, loc, race_no=str(i))
        if not success:
            break
        i += 1


# Calculate the start and end dates
end_date = datetime.now()
start_date = end_date - timedelta(days=1 * 365)
dates = get_dates(start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d"))

# data should look like: [{'date': '2024/06/19', 'weekday': 'weds', 'loc':'ST'}, {'date': '2024/07/06', 'weekday': 'sat', 'loc': 'HV'}...]
print(f"{dates=}")

# Use ThreadPoolExecutor to scrape races in parallel
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(scrape_race_for_date, date) for date in dates]

    for future in as_completed(futures):
        try:
            data = future.result()
        except Exception as exc:
            print(f"Generated an exception: {exc}")
