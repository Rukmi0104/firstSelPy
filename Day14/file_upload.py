# upload file you can manage with input tag using send_keys
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

location = r"D:\SeleniumPython\Projects\FITA\orders.xlsx"
serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()

# Navigate to products # dropdown type1 without select tag. With Ul or Li tag
sleep(5)
driver.find_element(By.XPATH, "//ul[@role='menu']/li[3]/a/p[contains(text(), 'Sales')]").click()
sleep(1)
driver.find_element(By.XPATH, "//ul[@role='menu']/li[3]/ul/li/a/p[text()=' Orders']").click()
sleep(4)
driver.find_element(By.NAME, "importexcel").click()
sleep(2)

driver.find_element(By.NAME, "importexcelfile").send_keys(location)

time.sleep(3)


