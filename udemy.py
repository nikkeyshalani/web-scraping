import requests
from bs4 import BeautifulSoup

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#getting the html from website
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page = requests.get(url)#asking can we grab the html

#print(page) o/p <Response [200]>  say you are aalow to get the data  if not 200 then you are not allowed

soup = BeautifulSoup(page.text,'lxml') #grabing html here as a text or vry long string. lxml puts the text back into html format 
#print(soup.prettify)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#tags
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# see header tag

#print(soup.header)

#only want div from heade
#print(soup.header.div)

#nevigable string
#text in p tag called nevigator string

#tag = soup.header.p #<p>Web Scraper</p>

#print(tag.string)#Web Scraper

#attributes  
#tag = soup.header.a 
#print(tag.attrs)#{'data-toggle': 'collapse-side', 'data-target': '.side-collapse', 'data-target-2': '.side-collapse-container'}
#print(tag['data-toggle'])#collapse-side
"""
attributte new atribute

tag['s'] = 'new'
print(tag.attrs)

"""

#find
#powerful function it is a filter function 


#print(soup.find('header')) # wxcatly like print(soup.header)
# then why we need this so if you check inside header tag lots of div tag available if we want to 4th div takg then find comes into the picture

#print(soup.find('div', {'class':"container test-site"}))#tag with attribute

#application find price
#print(soup.find('h4', {'class':"pull-right price"}).string)#$24.99

#only for class attribut

#print(soup.find('h4', class_="pull-right price").string)#$24.99

#all the prices are inside the same tag and same class then how to ditinques it i]and i get only29.99 the and in next find_all()
#everything similar on webpahge have same html code
"""
print(soup.find_all('h4', class_="pull-right price"))[<h4 class="pull-right price">$24.99</h4>, <h4 class="pull-right price">$57.99</h4>, <h4 class="pull-right price">$93.99</h4>, <h4 class="pull-right price">$109.99</h4>, <h4
class="pull-right price">$118.99</h4>, <h4 class="pull-right price">$499.99</h4>, <h4 class="pull-right price">$899.99</h4>, <h4 class="pull-right price">$899.99</h4>, <h4 class="pull-right price">$899.99</h4>]
"""
for i in soup.find_all('h4', class_="pull-right price"):
    print(i.string)
"""
o/p 
$24.99
$57.99
$93.99
$109.99
$118.99
$499.99
$899.99
$899.99
$899.99
"""

#print product mname

print(soup.find_all('a',class_="title"))

for i in soup.find_all('a',class_="title"):
    print(i.string)
"""
Nokia 123
LG Optimus
Samsung Galaxy
Nokia X
Sony Xperia
Ubuntu Edge
Iphone
Iphone
Iphone
"""

print(soup.find_all(['h4','p']))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#if we want to find all thge html code thst has id as an attribute
print(soup.find_all(id=True))

print(soup.find_all(string = "Iphone"))#['Iphone', 'Iphone', 'Iphone']

import re

print(soup.find_all(string = re.compile('Iph')))#['Iphone', 'Iphone', 'Iphone']
print(soup.find_all(string = re.compile('Nokia')))#['Nokia 123', 'Nokia X']
print(soup.find_all(class_ = re.compile('pull')))
print(soup.find_all('p',class_ = re.compile('pull')))#only give review


#first three review
print(soup.find_all('p',class_ = re.compile('pull'), limit= 3))

#product table

pro_name = soup.find_all('a',class_='title')
print(pro_name)

names=[]
for i in pro_name:
    names.append(i.text)

price = soup.find_all('h4', class_ = "pull-right price")
prices=[]
for i in price:
    prices.append(i.text)


review = soup.find_all('p',class_ = "pull-right")
reviews=[]
for i in review:
    reviews.append(i.text)


dis = soup.find_all('p',class_ = 'description')
disc=[]
for i in dis:
    disc.append(i.text)

import pandas as pd

table = pd.DataFrame({"product name":names,"discription":disc,"price":prices,"reviews":reviews})
print(table)

#extracting nested html
#we only want the add the detail of third product only
#insted of using soup which uses entire html why dont we use html of the box\

box = soup.find_all('div', class_= "col-sm-4 col-lg-4 col-md-4")
n = []
p = []
r=[]
d = []
for i in box:
    n.append(i.find('a').text)
    p.append(i.find('h4', class_ = "pull-right price").text)
    r.append(i.find('p',class_ = "pull-right").text)
    d.append(i.find('p',class_ = 'description').text)
print(n)
print(d)
print(r)
print(p)



