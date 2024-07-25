import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


url = os.getenv("TARGET_URL")

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if columns:
        rows.append([column.text.strip() for column in columns])

df = pd.DataFrame(rows, columns=headers)

print(df)

df.to_csv('racing_results.csv', index=False)