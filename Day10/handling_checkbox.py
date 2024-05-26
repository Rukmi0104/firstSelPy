import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

# Navigate to products

driver.find_element(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(), 'Catalog')]").click()
driver.find_element(By.XPATH, "//ul[@role= 'menu']/li[2]/ul/li/a/p[contains(text(), 'Products')]").click()
time.sleep(3)

# # click all checkbox using mastercheck box
wait_obj = WebDriverWait(driver, 10)
# wait_obj.until(ec.presence_of_all_elements_located((By.XPATH, "//th[@class= 'sorting_disabled text-center']/input[@class='mastercheckbox']")))
# driver.find_element(By.XPATH, "//th[@class= 'sorting_disabled text-center']/input[@class='mastercheckbox']").click()
# time.sleep(10)

# # click multiple checkboxes one by one using for loop
wait_obj.until(ec.presence_of_all_elements_located((By.XPATH, "//input[@name='checkbox_products']")))
check_elem1 = driver.find_elements(By.XPATH, "//input[@name='checkbox_products']")
for e1 in check_elem1:
    e1.click()

# move to next
wait_obj.until(ec.presence_of_element_located((By.XPATH, "//a[@data-dt-idx='2']")))
driver.find_element(By.XPATH, "//a[@data-dt-idx='2']").click()

time.sleep(3)
wait_obj.until(ec.presence_of_all_elements_located((By.XPATH, "//input[@name='checkbox_products']")))
check_elem2 = driver.find_elements(By.XPATH, "//input[@name='checkbox_products']")
for e2 in check_elem2:
    e2.click()


# click the checkboxes according to certain conditions. Ex. based on price range

price_val = driver.find_elements(By.XPATH, "//table[@id='products-grid']/tbody/tr/td[5]")

# # getting all price value using text. All values are in string form
# for p in price_val:
#     print(type(p.text))
#     if p.text != "":
#         print(p.text)

# # compare price with some condition and print value
# for p in price_val:
#     if p.text != "":
#         if float(p.text) >= 1000:
#             print(p.text)

# compare price with some condition and click the checkboxes
# row_count = driver.find_elements(By.XPATH, "//table[@id='products-grid']/tbody/tr/td[5]")
#
# for row in range(1, len(row_count)+1):
#     price = driver.find_element(By.XPATH, f"//table[@id='products-grid']/tbody/tr[{row}]/td[5]")
#     if price.text != "" and float(price.text) >= 1000:
#         # driver.find_element(By.XPATH, f"//table[@id ='products-grid']/tbody/tr[{row}]/td[1]").click()
#         #OR
#         driver.find_element(By.XPATH, f"//table[@id ='products-grid']/tbody/tr[{row}]/td[1]/input").click()
#
#         print(price.text)
#
# time.sleep(10)
