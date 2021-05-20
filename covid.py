#importing libraries

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import numpy as np

extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['S No.', 'State', 'Active', 'Cured', 'Death', 'Total']

response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))

stats = []
all_rows = soup.find_all('tr')

for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if stat:
        if len(stat) == 6:
# last row
            stat = [" ", *stat]
            stats.append(stat)
        elif len(stat) == 5:
            stats.append(stat)

stats[-1][1] = "ALL ADDED UP"

#stats.remove(stats[-1])

objects = []
for row in stats :
    objects.append(row[1])

y_pos = np.arange(len(objects))

#performance = []
#for row in stats:
 #   performance.append(int(row[2]) + int(row[3]))

table = tabulate(stats, headers=SHORT_HEADERS)
print(table)
print('--------------------------------------------------------------------------------------------------')
print(stat)

input()