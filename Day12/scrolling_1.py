import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demoqa.com/accordian")

# scroll on horizontal to right side and vertical to down
action = ActionChains(driver)
action.scroll_by_amount(100, 200).perform()
time.sleep(3)
