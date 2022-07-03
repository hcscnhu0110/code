from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_experimental_option("detach", True)
    path = "C:/Users/user/Desktop/chromedriver.exe" 
    service = Service(path)
    driver = webdriver.Chrome(options = options, service = service)
    return driver

def login(driver, wait) :
    driver.switch_to.frame(driver.find_element_by_name("bookmark"))
    id = wait.until(EC.presence_of_element_located((By.NAME, "id")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    login = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/font/center/form/table/tbody/tr[6]/td/input[1]")))

    id.clear()
    password.clear()
    id.send_keys("410410091")
    password.send_keys("_Zone12345")
    login.click()

    plus = wait.until(EC.presence_of_element_located((By.ID, "itemTextLink4")))
    plus.click()

def choose(driver, wait) :
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("basefrm"))
    target1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='form1']/table/tbody/tr[2]/td/table/tbody/tr[2]/td[8]/font/input[2]")))
    target1.click()
    target2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='cge_cate2']")))
    target2.click()
    target3 = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='cge_subcate2']/input[2]")))
    target3.click()
    submit = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='form1']/input[6]")))
    submit.click()

def main() :
    driver = create_driver()
    driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/")
    wait = WebDriverWait(driver, 10)
    login(driver, wait)
    choose(driver, wait)

if __name__ == '__main__' :
    main()
    