import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.espn.com/nba/statistics/player/_/stat/assists/sort/avgAssists/year/2017/seasontype/2'
headers = {'User-Agent': 'Mozilla/5.0'}

source = requests.get(url, headers = headers)

soup = BeautifulSoup(source.content, 'html.parser')

stat_table = soup.find_all('table', class_='tablehead')
stat_table = stat_table[0]

rows = stat_table.find_all('tr') # ALL ROWS
header = [tr.text.strip() for tr in rows[0].find_all('td')] # this is a ROW, too
other_rows = rows[1:] # ALL OTHER rows

csv_file = open('NBA_Stats.csv', 'w') # create a csv file
writer = csv.writer(csv_file) # write to the csv file
writer.writerow(header) # write the header, just once
for row in other_rows: # now, loop through all other rows
    data = [tr.text.rstrip() for tr in row.find_all('td')]
    writer.writerow(data)
csv_file.close()

