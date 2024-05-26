import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_ojb)
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()

# Navigate to products # dropdown type1 without select tag. With Ul or Li tag
driver.find_element(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(), 'Catalog')]").click()
driver.find_element(By.XPATH, "//ul[@role= 'menu']/li[2]/ul/li/a/p[contains(text(), 'Products')]").click()
time.sleep(3)

# Select dropdown
# import select class, pass the element to click on the dropdown
drp_ele = driver.find_element(By.XPATH, "//select[@name='products-grid_length']")
select = Select(drp_ele)
select.select_by_value("20")
time.sleep(3)
select.select_by_index(1)   # indexing starts from 0. work on python rule from 0 to n-1
time.sleep(4)
select.select_by_visible_text('100')
time.sleep(5)

# select.deselect_all()   # NotImplementedError("You may only deselect all options of a multi-select")
# time.sleep(5)

# select.deselect_by_value('20')  # NotImplementedError("You may only deselect all options of a multi-select")




