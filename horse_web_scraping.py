import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("TARGET_URL")
results_folder_url =os.getenv("RESULTS_FOLDER")


response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

# Use CSS selector to find the first specific table
table1 = soup.select_one("#innerContent > div.localResults.commContent.fontFam > div:nth-child(5) > table > tbody")

# Extract table headers for the first table
headers1 = [header.text.strip() for header in table1.find_all('th')]

# Extract table rows for the first table
rows1 = []
for row in table1.find_all('tr'):
    columns = row.find_all('td')
    if columns:
        rows1.append([column.text.strip() for column in columns])

df1 = pd.DataFrame(rows1, columns=headers1 if headers1 else None)
print(df1)
df1.to_csv(f'{results_folder_url}racing_results_table1.csv', index=False)

# Use CSS selector to find the second specific table
table2 = soup.select_one("#innerContent > div.localResults.commContent.fontFam > div.race_tab > table")

# Extract table headers for the second table
headers2 = [header.text.strip() for header in table2.find_all('th')]

# Extract table rows for the second table
rows2 = []
for row in table2.find_all('tr'):
    columns = row.find_all('td')
    if columns:
        rows2.append([column.text.strip() for column in columns])

df2 = pd.DataFrame(rows2, columns=headers2 if headers2 else None)
print(df2)
df2.to_csv(f'{results_folder_url}racing_results_table2.csv', index=False)