import requests
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#company name
name = soup.find('h1', class_ = 'company__name')
#current price of the stock
price = soup.find('bg-quote', class_ = 'value').text
#print(price)

#closing price of the tag
closing_price = soup.find('td', class_ = 'table__cell u-semi').text
#print(closing_price,type(closing_price))

#52 weak range

nested = soup.find('mw-rangebar', class_= "element element--range range--yearly")
n = nested.find_all('span', class_ = 'primary')
range=[]
for i in n:
    range.append(i.text)

#print(max_range)

#analyst rating
rating = soup.find('li', class_='analyst__option active').text

import pandas as pd
table = pd.DataFrame({"company name": name,"stock_price":price,"closing_price": closing_price,"52 weak range" : range,"analytical rating": rating})

print(table)