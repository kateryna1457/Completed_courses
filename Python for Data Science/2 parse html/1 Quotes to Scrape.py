Sourse:
view-source:https://quotes.toscrape.com/

Task:
fill all most common words in quotes
-----------------------------

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_= 'tag-item')
for quote in quotes:
    print(quote.text)

