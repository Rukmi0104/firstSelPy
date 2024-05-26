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

# select 100 from the 'Show' dropdown and check all checkboxes
# Steps 1: select 100 from the 'Show' dropdown
drp_ele = driver.find_element(By.XPATH, "//select[@name='products-grid_length']")
select = Select(drp_ele)
select.select_by_visible_text("100")

time.sleep(5)

# Steps 2: check all checkboxes whose price is greater than or equal to 1000
row_count = driver.find_elements(By.XPATH, "//table[@id = 'products-grid']/tbody/tr/td[5]")
prod_name = driver.find_elements(By.XPATH, "//table[@id = 'products-grid']/tbody/tr/td[3]")
time.sleep(10)
for row in range(1, len(row_count)+1):
    price = driver.find_element(By.XPATH, f"//table[@id = 'products-grid']/tbody/tr[{row}]/td[5]")
    if price.text != "" and float(price.text) >= 1000:
        driver.find_element(By.XPATH, f"//table[@id = 'products-grid']/tbody/tr[{row}]/td[1]").click()
        print(driver.find_element(By.XPATH, f"//table[@id = 'products-grid']/tbody/tr[{row}]/td[3]").text)
        print(driver.find_element(By.XPATH, f"//table[@id = 'products-grid']/tbody/tr[{row}]/td[5]").text)
# for p in prod_name:
#     print(p.text)

time.sleep(5)
