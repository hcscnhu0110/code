import json
from bs4 import BeautifulSoup as bs
import requests
import re

url = input()
html = requests.get(url)
soup = bs(html.text, 'html.parser')
p = re.compile('var ytInitialData = (.*?);$',re.MULTILINE | re.DOTALL)
script = soup.find("script", text = p)
print(p.search(script.text).group(1))

#with open('html_script.txt','w',encoding = 'utf-8') as f :
  #  print(x,file = f)