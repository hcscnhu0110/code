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
options.add_experimental_option("excludeSwitches" , ['enable-logging'])             #忽略連結失去作用那個無用文本
options.add_experimental_option("detach", True)                                     #讓打開的google不會自己關
path = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"          
service = Service(path)                                                             #以免DeprecationWaring 版本問題
driver = webdriver.Chrome(options = options , service = service) 
driver.get("https://accounts.spotify.com/zh-TW/login?continue=https%3A%2F%2Fopen.spotify.com%2F")

wait = WebDriverWait(driver , 10)
username = wait.until(EC.presence_of_element_located((By.ID , "login-username")))
password = wait.until(EC.presence_of_element_located((By.ID , "login-password")))
login = driver.find_element_by_xpath("//*[@id='login-button']/div[1]/p")

username.clear()
password.clear()

username.send_keys("twynnn9@gmail.com")
password.send_keys("know6868")
login.click()

time.sleep(5)

search = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/nav/div[1]/ul/li[2]/a")
search.click()

time.sleep(5)

style = driver.find_element_by_xpath("//*[@id='searchPage']/div/div/div/section/div[2]/a[49]")
style.click()

time.sleep(5)

titles = driver.find_elements_by_class_name("Nqa6Cw3RkDMV8QnYreTr")
for title in titles :
    print(title.text)
