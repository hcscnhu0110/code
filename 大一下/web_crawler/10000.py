from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches" , ['enable-logging'])             
options.add_experimental_option("detach", True)                                     
path = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"          
service = Service(path)                                                             
driver = webdriver.Chrome(options = options , service = service) 
driver.get("https://open.spotify.com/playlist/1G8IpkZKobrIlXcVPoSIuf")
wait = WebDriverWait(driver , 20)


count = wait.until(EC.presence_of_element_located((By.XPATH , "/html/head/meta[195]"))).get_attribute("content") 
mix = list()
song_name = list()
artist_name = list()
duration = list()
while True :
    songs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "t_yrXoUO3qGsJS4Y6iXX")))
    artists = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "rq2VQ5mb9SDAFWbBIUIn")))
    durations = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "Btg2qHSuepFGBG6X0yEN")))
    l = len(artists)
    for x , y , z in zip(songs , artists , durations) :
        if [x.text , y.text , z.text] not in mix :
            mix.append([x.text , y.text , z.text])
    driver.execute_script("arguments[0].scrollIntoView();" , artists[l-1])
    time.sleep(3)
    num = len(mix)
    if num == int(count) or num >= 9990 :
        for i in range(num) :
            song = mix[i][0]
            if '(' in song :
                song = song[:mix[i][1].find('(')]
            song_name.append(song)
            artist = mix[i][1]
            if ',' in artist :
                artist = artist.replace(',' , '&')
            artist_name.append(artist)
            Time = mix[i][2]
            duration.append(Time)
        break

with open('song_name.txt' , 'w' ,encoding = 'utf-8') as f :      
    for i in song_name :
        f.write(i + '\n')
with open('artist_name.txt' , 'w' ,encoding = 'utf-8') as f :      
    for i in artist_name :
        f.write(i + '\n')
with open('duration.txt' , 'w' ,encoding = 'utf-8') as f :      
    for i in duration :
        f.write(i + '\n')