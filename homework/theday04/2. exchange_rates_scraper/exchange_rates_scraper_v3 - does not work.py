# Get data from website
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content)  # Parse the HTML as a string

table = soup.find_all('<table')[41]  # Grab the first table

new_table = pd.DataFrame(columns=range(0, 3), index=[0])

row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_marker, column_marker] = column.get_text()
        column_marker += 1

new_table


