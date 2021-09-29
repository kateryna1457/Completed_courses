from datetime import datetime
from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    i = soup('i', {'class': 'date'})
    if not i:
        raise ValueError('fail to find the date')

    date = datetime.strptime(i[0].text, '%Y-%m-%d')

    rates = {}
    for tr in soup('tr'):
        symbol_td, rate_td = tr('td')
        symbol = symbol_td('i')[0]['title']
        rate = float(rate_td.text)
        rates[symbol] = rate

    return date, rates

with open(r'D:\Epam\Self_study\Python for Data Scientists\Exercise Files\Ch04\04_02\fx.html') as fp:
    html = fp.read()

date, rates = parse_html(html)
print(f'date: {date}')
for symbol, rate in rates.items():
    print(f'USD/{symbol} = {rate:f}')
