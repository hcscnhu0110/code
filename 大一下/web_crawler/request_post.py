import requests
from bs4 import BeautifulSoup as bs
url = "https://ani.gamer.com.tw/"

headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}

r = requests.post(url , headers = headers)

with open("spotify.txt" , 'w' , encoding = 'utf-8') as f :
    f.write(r.text)