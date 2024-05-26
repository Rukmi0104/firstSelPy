import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
driver.implicitly_wait(10)

dt1= datetime.datetime(2024, 7, 9)
year = dt1.strftime("%Y")
month = dt1.strftime("%m")
date = dt1.strftime("%d")

driver.find_element(By.XPATH, "//img[@class='imgdp']").click()
month_ele = driver.find_element(By.ID, "//span[@class='ui-datepicker-month']")
year_ele = driver.find_element(By.ID, "//span[@class='ui-datepicker-year']")


