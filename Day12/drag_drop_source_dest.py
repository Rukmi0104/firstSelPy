import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

action = ActionChains(driver)

######################################
# perform drag and drop operation when source and destination locator is given
source_elem = driver.find_element(By.ID, "box2")
dest_elem = driver.find_element(By.ID, "box102")
action.drag_and_drop(source_elem, dest_elem).perform()
time.sleep(2)




