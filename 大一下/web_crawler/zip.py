import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches" , ['enable-logging'])             
options.add_experimental_option("detach", True)                                     
path = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"          
service = Service(path)                                                             
driver = webdriver.Chrome(options = options , service = service) 
driver.get("https://open.spotify.com/playlist/37i9dQZF1DX4XkcocBAgP3")
wait = WebDriverWait(driver , 20)

artist_name = list()
mix = list()
count = wait.until(EC.presence_of_element_located((By.XPATH , "/html/head/meta[195]"))).get_attribute("content") 
while True :
    artists = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "rq2VQ5mb9SDAFWbBIUIn")))
    time.sleep(5)
    songs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "t_yrXoUO3qGsJS4Y6iXX")))
    time.sleep(5)
    durations = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "Btg2qHSuepFGBG6X0yEN")))
    time.sleep(5)
    l = len(artists)
    for x , y , z in zip(songs , artists , durations) :
        if [x.text , y.text , z.text] not in mix :
            mix.append([ x.text , y.text , z.text])
    
    print(mix)
    driver.execute_script("arguments[0].scrollIntoView();" , artists[l-1])
    time.sleep(5)
    num = len(mix)
    if  num == int(count):
        for i in range(num) :
            artist = mix[i][1]
            artist_name.append(artist)
        break

