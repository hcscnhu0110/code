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
driver.get("https://www.google.com")
wait = WebDriverWait(driver , 20)



def find_info(song_name , artist_name , duration) :
    mix = list()
    count = wait.until(EC.presence_of_element_located((By.XPATH , "/html/head/meta[195]"))).get_attribute("content") 
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
        if  num == int(count):
            for i in range(num) :
                song = mix[i][0]
                if '(' in song :
                    song = song[:mix[i][1].find('(')]
                song_name.append(song)
                artist = mix[i][1]
                artist_name.append(artist)
                Time = mix[i][2]
                duration.append(Time)
            break

def main() :
    singers = list()
    with open('singer.txt' , 'r' , encoding = 'utf-8') as f :
        singers = f.readlines()
    song_name = list()
    artist_name = list()
    duration = list()
    for i in range(8,21) :
        search_singer = wait.until(EC.presence_of_element_located((By.NAME , 'q')))
        name = singers[i].rstrip('\n')
        keyword = "This is" + " " + name + " " + "spotify playlist"
        search_singer.send_keys(keyword)
        search_singer.send_keys(Keys.RETURN)
        websites = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME , 'h3')))
        aim = 0
        for i in range(len(websites)) :
            if 'This Is' in websites[i].text :
                aim = i
                break
        websites[aim].click()
        check = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "t_yrXoUO3qGsJS4Y6iXX")))
        if check[1].text == check[0].text :
            driver.back()
            search_singer = wait.until(EC.presence_of_element_located((By.NAME , 'q')))
            search_singer.clear()
        else :
            find_info(song_name , artist_name , duration)
            time.sleep(3)
            driver.back()
            search_singer = wait.until(EC.presence_of_element_located((By.NAME , 'q')))
            search_singer.clear()
    
    x = 1
    y = 1
    z = 1
    with open('song_name.txt' , 'w' ,encoding = 'utf-8') as f :      
        for i in song_name :
            f.write(str(x) + '\n')
            f.write(i + '\n')
            x = x+1
    with open('artist_name.txt' , 'w' ,encoding = 'utf-8') as f :      
        for i in artist_name :
            f.write(str(y) + '\n')
            f.write(i + '\n')
            y = y+1
    with open('duration.txt' , 'w' ,encoding = 'utf-8') as f :      
        for i in duration :
            f.write(str(z) + '\n')
            f.write(i + '\n')
            z = z+1

main()