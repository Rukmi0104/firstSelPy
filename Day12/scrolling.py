import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(10)

action = ActionChains(driver)
# scrolling until element found
Ind_flag = driver.find_element(By.XPATH, "//td[text()='India']")
action.scroll_to_element(Ind_flag).perform()
print(Ind_flag.location)
time.sleep(3)

 #  scrolling from some defined origin
scroll_origin = ScrollOrigin.from_element(Ind_flag)
action.scroll_from_origin(scroll_origin, 0, 1000).perform()
time.sleep(5)

# scroll by amount

action.scroll_by_amount(0, 3000).perform()
time.sleep(4)

action.scroll_by_amount(0, -3000).perform()
time.sleep(4)
