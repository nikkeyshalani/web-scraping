import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.airbnb.co.in/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&query=Honolulu%2C%20HI&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-07-20&checkout=2022-07-21&adults=2&source=structured_search_input_header&search_type=autocomplete_click"
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')




df = pd.DataFrame({'Link':[''], 'Title':[''], 'Price':[''], 'Details':[''],"Rating":[""]})
c = 0
while c<14:
    posting= soup.find_all('div', class_="c4mnd7m dir dir-ltr")
    for post in posting:
        try:
            link = post.find('a', class_='ln2bl2p dir dir-ltr').get('href')
            link_full = "https://www.airbnb.co.in" + link
            title = post.find('div', class_= "t1jojoys dir dir-ltr").text
            detail = post.find('span',class_='dir dir-ltr').text
            price = post.find('span',class_='a8jt5op dir dir-ltr').text
            rating = post.find('span',class_="ru0q88m dir dir-ltr").text
            df = df.append({'Link':link_full, 'TItle':title, 'Price':price, 'Details':detail,"Rating":rating}, ignore_index = True)
            
        except:
            pass
    #next_page = soup.find('a',{'aria-label':'Next'}).get('href')
    try:
        next_page = soup.find_all('a', {'aria-label':'Next'})[1].get('href')
    except:
        next_page = soup.find('a', {'aria-label':'Next'}).get('href')
    next_page_full= "https://www.airbnb.co.in" + next_page
    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    c+=1
    print(c)
    

df.to_csv('airbnb.csv')



