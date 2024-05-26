# time.sleep('time in sec')
# driver.implicit_wait('time in sec')
# driver.explicit_wait
# sometimes system processor or webpage is slow and taking time to load. But, selenium will be checking all the element
# very quickly. SO there will be mismatch in the browser speed and webdriver speed. In such case error may occur.
# we call it as sync time error. we can avoid those error by giving sleep time.
# But time.sleep is not a coding standard. Also, with time.sleep we can provide hard sleep which will unnecessary
# keep waiting application for given time. Sometimes browser will not that much time to load.
# so time.sleep is not used mostly.

# So, there are 2 ways to implement wait in selenium. implicit and explicit wait.
# usually for dropdown and radio buttons we need to apply waits as it takes time to load than other elements.

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

## launch chrome driver
service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_ojb)
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()
driver.find_element(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(),  'Sales')]").click()

# fetch all text from Sales list --> using time.sleep -->Working fine
# time.sleep(3)

# SalesList = driver.find_elements(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(),  'Sales')]/parent::a/following-sibling::ul/li/a/p")
# for s in SalesList:
#     print(s.text)


# # fetch all text from Sales list --> using implicitly_wait-->not Working fine
# #IF TIME.SLEEP OF 3 SEC IS WORKING THEN IMPLICIT WAIT of 10 sec SHOULD ALSO WORK ?
driver.implicitly_wait(10)
# time.sleep(3)
SalesList = driver.find_elements(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(),  'Sales')]/parent::a/following-sibling::ul/li/a/p")
for s in SalesList:
    print(s.text)

# fetch all text from Sales list --> using explicit wait--> sometimes it works and sometimes not

# wait_obj = WebDriverWait(driver, 300)
# wait_obj.until(ec.presence_of_all_elements_located((By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(),  'Sales')]/parent::a/following-sibling::ul/li/a/p")))
# SalesList = driver.find_elements(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(),  'Sales')]/parent::a/following-sibling::ul/li/a/p")
# # time.sleep(10)
# for s in SalesList:
#     print(s.text)


