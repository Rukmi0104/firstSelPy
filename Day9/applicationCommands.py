import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"D:\SeleniumPython\Projects\FITA\msedgedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)

