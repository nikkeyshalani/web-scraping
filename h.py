from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

from requests import request
import requests
import sendemail

req = requests.get('https://www.ndtv.com/')


soup = BeautifulSoup(req.content, "lxml")


links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))


def link_alert(price):
    message = f"The Price of the item you were looking for has now dropped to {price}"
    sendemail.send_email(message, sender_email, sender_password, receiver_email)
sender_email = input("Enter the Email from which you want to get notified: ")
sender_password = input("Enter the password of the Email from which you want to get notified: ")
receiver_email = input("Enter the email to which you want to get notified(can be the same as your sender email): ")
link_alert(links)