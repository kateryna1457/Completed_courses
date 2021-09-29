Source:
view-source:https://en.wikipedia.org/wiki/Adolf_(disambiguation)

Task:
print all headers of found articles for search "Adolf" and the descriprion to these articles
---------------------------------

import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Adolf_(disambiguation)'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

titel = re.compile('^(Adol)')

quotes = soup.find_all('a', text = titel)

li = soup.find_all('li')

for element  in li:
    for i in element('a'):
        if i in quotes:
            print(element.text)
