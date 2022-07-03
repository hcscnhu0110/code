from bs4 import BeautifulSoup as bs
import requests
import re

url = input()
r = requests.get(url)
html = r.text
soup = bs(html,'html.parser')
with open('html.txt','w',encoding = 'utf-8') as f :
    print(soup.prettify(),file = f)
