import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7"
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')

#df = pd.DataFrame({"link":[""],"title":[""],"detail":[""],"price":[""],"color":[""]})

df = pd.DataFrame({'Link':[''],'Name':[''], 'Price':[''], 'Color':['']})
c = 0
while c<15:
    posting= soup.find_all('div', class_="media soft push-none rule")
    
    for post in posting:
        link = post.find('a', class_ ='media__img media__img--thumb').get('href')
        full_link = 'https://www.carpages.ca'+link
        

        title = post.find('h4', class_ ='hN').text.strip()
        price = post.find('strong',class_='delta').text.strip()
        color = post.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        df = df.append({'link':full_link,'Name':title, 'Price':price, 'Color':color},ignore_index=True)
    next_page = soup.find('a', class_ = 'nextprev').get('href')
    next_page_full = 'https://www.carpages.ca'+ next_page
    page = requests.get(next_page_full)
    soup = BeautifulSoup(page.text, 'lxml')
    
    c+=1
df.to_csv("used_car_detail.csv")

