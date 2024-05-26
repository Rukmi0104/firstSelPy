
# from console we can execute script also
# we can us java script commands to execute
# to execute Java commands we have to use driver.execute_script
# if you have any id, classname, name, tagname then we can use document.getElementBy.. ex we used for locating email and password field
# if we dont have any of above options, then we have to use driver object. Ex for locating and clicking login button.


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/")
driver.implicitly_wait(10)

# clear existing text from email
driver.execute_script("document.getElementById('Email').value=''")
time.sleep(1)
driver.execute_script("document.getElementById('Email').value='admin@yourstore.com'")
time.sleep(1)
driver.execute_script("document.getElementById('Password').value=''")
time.sleep(1)
driver.execute_script("document.getElementById('Password').value='admin'")
time.sleep(1)

login_web_element = driver.find_element(By.CLASS_NAME, "login-button")
driver.execute_script("arguments[0].click()", login_web_element)

