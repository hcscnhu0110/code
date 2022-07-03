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



def find_song(song_name) :
    songlist = list()
    count = wait.until(EC.presence_of_element_located((By.XPATH , "/html/head/meta[195]"))).get_attribute("content") 
    while True :
        songs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "t_yrXoUO3qGsJS4Y6iXX")))
        l = len(songs)
        for i in songs :
            if i.text not in songlist :
                songlist.append(i.text)
        driver.execute_script("arguments[0].scrollIntoView();" , songs[l-1])
        time.sleep(5)
        num = len(songlist)
        if  num == int(count):
            for i in range(num) :
                song = songlist[i]
                if '(' in song :
                    song = song[:songlist[i].find('(')]
                song_name.append(song)
            break

def main() :
    singers = list()
    with open('singer.txt' , 'r' , encoding = 'utf-8') as f :
        singers = f.readlines()
    song_name = list()
    for i in range(2) :
        search_singer = wait.until(EC.presence_of_element_located((By.NAME , 'q')))
        name = singers[i].rstrip('\n')
        keyword = name + " " + "spotify playlist"
        search_singer.send_keys(keyword)
        search_singer.send_keys(Keys.RETURN)
        website = wait.until(EC.presence_of_element_located((By.TAG_NAME , 'h3')))
        website.click()
        find_song(song_name)
        time.sleep(3)
        driver.back()
        search_singer = wait.until(EC.presence_of_element_located((By.NAME , 'q')))
        search_singer.clear()
    x = 1
    with open('song_name.txt' , 'w' ,encoding = 'utf-8') as f :      
        for i in song_name :
            f.write(str(x) + '\n')
            f.write(i + '\n')
            x = x+1

main()


'''
search_singer = wait.until(EC.presence_of_element_located((By.NAME , 'q')))
name = singers[0].rstrip('\n')
keyword = name + " " + "spotify playlist"
search_singer.send_keys(keyword)
search_singer.send_keys(Keys.RETURN)
website = wait.until(EC.presence_of_element_located((By.TAG_NAME , 'h3')))
website.click()
time.sleep(5)
'''

# driver.execute_script("window.scrollTo(0 , document.body.scrollHeight);")

#js = "var q=document.getElementsByClassName('os-scrollbar-handle')[0].scrollTop=10000"
#driver.execute_script(js)
    
#Times = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "Btg2qHSuepFGBG6X0yEN")))
#print(Times[0].text)

#artist = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "rq2VQ5mb9SDAFWbBIUIn")))
#print(artist[].text)