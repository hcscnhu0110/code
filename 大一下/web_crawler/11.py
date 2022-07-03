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
driver.get("https://www.google.com/search?q=This+is+Arcade+Fire+spotify+playlist&source=hp&ei=Ol2GYv-4A5DJ2roPpOGNmAY&iflsig=AJiK0e8AAAAAYoZrSo6HbC8xxAcffxNYU0bR2uLc4JbD&ved=0ahUKEwj_vZzg6-v3AhWQpFYBHaRwA2MQ4dUDCAk&uact=5&oq=This+is+Arcade+Fire+spotify+playlist&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABOgcIIRAKEKABUABYhAJg6AJoAHAAeACAAUWIAfYBkgEBNJgBAKABAQ&sclient=gws-wiz")
wait = WebDriverWait(driver , 20)

web = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME , "h3")))
