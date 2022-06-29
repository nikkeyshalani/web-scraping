import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.nfl.com/standings/league/2019/REG"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")\


tab = soup.find('table', summary="Standings - Detailed View")
header = []
for i in soup.find_all('th'):
    header.append(i.text)
df = pd.DataFrame(columns=header)


for row in tab.find_all('tr')[1:]:
    #line below fixes the formatting issue we had with the team names
    first_td = row.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0,first_td)
    length = len(df)
    df.loc[length] = row_data

df.to_csv('assign.csv')




