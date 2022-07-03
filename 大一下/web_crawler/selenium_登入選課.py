import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time


options = webdriver.ChromeOptions()                                #設置為開發者模式 以防被一些識別到使用selenium
options.add_experimental_option("excludeSwitches" , ['enable-logging'])         #忽略連結失去作用那個無用文本
options.add_experimental_option("detach", True)                                     #讓打開的google不會自己關
path = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"          
service = Service(path)                                                             #以免DeprecationWaring 版本問題
driver = webdriver.Chrome(options = options , service = service) 
driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/")

driver.switch_to.frame(driver.find_element_by_name("bookmark")) #driver.switch_to.default_content() 切回來

wait = WebDriverWait(driver , 10)
id = wait.until(EC.presence_of_element_located((By.NAME , "id")))
password = wait.until(EC.presence_of_element_located((By.NAME , "password")))

login = driver.find_element_by_xpath("/html/body/font/center/form/table/tbody/tr[6]/td/input[1]")
id.clear()
password.clear()
id.send_keys("410410091")
password.send_keys("_Zone12345")
login.click()
