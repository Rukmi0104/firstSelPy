# copy and paste actions we can do using ActionChains class


import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.geeksforgeeks.org/")
driver.find_element(By.XPATH, "//a[(text()= 'Sign In') and (@type='button')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//label[text()= 'Sign Up']").click()
time.sleep(3)
driver.find_element(By.ID, "email").send_keys("abc.123@gmail.com")
action = ActionChains(driver)
# copy email id using "Ctrl +A" and copy the email using 'ctrl + c'
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

action.send_keys(Keys.TAB).perform()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

action.send_keys(Keys.TAB).perform()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)
