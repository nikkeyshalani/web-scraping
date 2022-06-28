import bs4
import requests
import urllib.request
import csv
from datetime import datetime
import time
import sendemail

 
url = "https://www.reliancedigital.in/hp-15s-fq4021tu-laptop-11th-gen-intel-core-i5-1155g7-8gb-512gb-ssd-intel-iris-xe-graphics-windows-11-home-mso-fhd-39-62-cm-15-6-inch-/p/492575363"
#r = str(requests.get(url)).split(" ")
#r = requests.get(URL)
#print(r)
#soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())

#print(type(title))#<class 'bs4.element.Tag'>  special type of object implemented by beautiful soup
#print(type(title.string))#<class 'bs4.element.NavigableString'>

#comenly used type of object
#1. tag
#2. NavigableString
#3. beautifulsoup


#print(type(soup)<class 'bs4.BeautifulSoup'>

#4. comment

#get title of htmal page
#title = soup.title
#get all the paragraph of the page
#paras = soup.find_all('p')
#print(paras)
#ass = soup.find_all("a")
#print(ass)

#p = soup.find('p')
#print(soup.find('p')['class'])
def get_url():
    url = input("Enter the URL of the product: ")
    response = str(requests.get(url)).split(" ")
    while response[1] != "[200]>":
        print("Invalid URL. Try Again.")
        url = input("Enter the URL of the product: ")
        response = str(requests.get(url)).split(" ")
    return url
def save_price(price_list):
    field = ['Time', 'Price']
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data = [[dt_string, str(price_list)]]
    with open("prices.csv", 'w') as price_file:
        writer = csv.writer(price_file)
        writer.writerow(field)
        writer.writerows(data)
def pricer(url):
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")
    try:
        price = float(soup.find(class_="pdp__offerPricehttps://www.re").get_text().replace("₹", "").replace(",", ""))
    except AttributeError():
        price = float(soup.find(class_="a-price-whole").get_text().replace(",", "").replace(".", ""))
    return price
def price_alert(price):
    message = f"The Price of the item you were looking for has now dropped to {price}"
    sendemail.send_email(message, 'sender_email', 'sender_password', "receiver_email")

def compare(price):
    sender_email = input("Enter the Email from which you want to get notified: ")
    sender_password = input("Enter the password of the Email from which you want to get notified: ")
    receiver_email = input("Enter the email to which you want to get notified(can be the same as your sender email): ")
    with open("prices.csv", "r") as price_file:
        reader = csv.reader(price_file)
        price_list = []
        for row in reader:
            price_list.append(row)
        price_list = price_list[-2]
        old_price = price_list[-1]
        if int(old_price)>price:
            price_alert(price, sender_email, sender_password, receiver_email)
            return True
        return False

def initfile():
    field = ['0', '0']
    data = [['0', '0']]
    with open("prices.csv", 'w') as price_file:
        writer = csv.writer(price_file)
        writer.writerow(field)
        writer.writerows(data)

print()
def main():
    decrease = False
    count = False
    while decrease==False:
        if count == False:
            initfile()
        url = get_url()
        price = pricer(url)
        decrease = compare(price)
        if decrease == False:
            save_price(price)
        count = True
        time.sleep(60*60*6)

if __name__ == '__main__':
    main()




