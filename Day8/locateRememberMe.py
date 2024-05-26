import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/")

# <label for="RememberMe" xpath="1">Remember me?</label>
# <input type="checkbox" data-val="true" data-val-required="The Remember me? field is required." id="RememberMe" name="RememberMe" value="true">

# by id
driver.find_element(By.ID, "RememberMe").click()
time.sleep(1)

# by name
driver.find_element(By.NAME, "RememberMe").click()
time.sleep(1)

##############################
# by css selector
# tagName#id
# tagName.className     -> class name is not present in the element so xpath can not be prepared using class name
# tagName[attribute = 'value']

# tagName#id
driver.find_element(By.CSS_SELECTOR, "input#RememberMe").click()
time.sleep(1)

# tagName[attribute = 'value']
driver.find_element(By.CSS_SELECTOR, "input[type= 'checkbox']").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[id = 'RememberMe']").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name = 'RememberMe']").click()
time.sleep(1)

#############################3
# click Remember Me using relative xpath
driver.find_element(By.XPATH, "//label[@for = 'RememberMe']").click()
time.sleep(1)

# OR
driver.find_element(By.XPATH, "//input[@type= 'checkbox']").click()
time.sleep(1)

# OR
driver.find_element(By.XPATH, "//input[@id = 'RememberMe']").click()
time.sleep(1)

# OR
driver.find_element(By.XPATH, "//input[@name = 'RememberMe']").click()
time.sleep(1)

#############################
# click Remember Me using absolute xpath
driver.find_element(By.XPATH, "html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[3]/input").click()
time.sleep(1)


#############################
# click Remember Me using contains, text and starts-with in xpath
driver.find_element(By.XPATH, "//*[contains(text(), 'Remember me?')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[contains(@id, 'RememberMe')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[contains(@name, 'RememberMe')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[contains(@type, 'checkbox')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[text()= 'Remember me?']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[starts-with(@id, 'Remember')]").click()
time.sleep(1)





