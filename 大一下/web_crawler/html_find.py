from bs4 import BeautifulSoup as bs
import requests
import re

with open('watch.htm','r',encoding = 'utf-8') as f :
    html = f.read()
soup = bs(html,'html.parser')
x = soup.find_all('link',href = re.compile("list=\w{34}"))
for i in x :
    s = i['href']
    t = re.search("list=\w{34}",s)
    print(t.group()[5:])