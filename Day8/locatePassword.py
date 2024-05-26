import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)

# Locate password by id
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("pass1")
time.sleep(3)

# Locate password by name
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("pass2")
time.sleep(3)

# locate password by class name
driver.find_element(By.CLASS_NAME, "password").clear()
driver.find_element(By.CLASS_NAME, "password").send_keys("pass3")
time.sleep(3)

##########################
# locate password by tag name
# this code will throw "selenium.common.exceptions.InvalidElementStateException:
# Message: invalid element state" as there are multiple elements with tagname "input".
# Everytime we have to give unique locator to identify the element.
# driver.find_element(By.TAG_NAME, "input").clear()
# driver.find_element(By.TAG_NAME, "input").send_keys("pass")
# time.sleep(3)

##########################
# locate password by link text
# there is no link text in description, so we can not use this locator?????
# driver.find_element(By.LINK_TEXT, "Password").clear()
# driver.find_element(By.LINK_TEXT, "Password").send_keys("pass")
# time.sleep(3)

# locate password by partial link text
# there is no link text in description, so we can not use this locator?????
# driver.find_element(By.PARTIAL_LINK_TEXT, "Password").clear()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Password").send_keys("pass")
# time.sleep(3)

# Locate password using Custom locators -> css and xpath
# CSS
# tag#id
# tag.classname
# tag[attribute= value]

driver.find_element(By.CSS_SELECTOR, "input#Password").clear()
driver.find_element(By.CSS_SELECTOR, "input#Password").send_keys("pass4")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "input.password").clear()
driver.find_element(By.CSS_SELECTOR, "input.password").send_keys("pass5")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "input[value= 'admin']").clear()
driver.find_element(By.CSS_SELECTOR, "input[value= 'admin']").send_keys("pass6")
time.sleep(3)

#OR
driver.find_element(By.CSS_SELECTOR, "input[class='password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[class='password']").send_keys("pass7")
time.sleep(3)

#OR
driver.find_element(By.CSS_SELECTOR, "input[type='password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("pass8")
time.sleep(3)

# OR
driver.find_element(By.CSS_SELECTOR, "input[id='Password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[id='Password']").send_keys("pass9")
time.sleep(3)

#OR
driver.find_element(By.CSS_SELECTOR, "input[name='Password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name='Password']").send_keys("pass10")
time.sleep(3)

# OR
# below code will work for email field as same attribute is available in email also.
# The first searched parameter is considered during execution
# driver.find_element(By.CSS_SELECTOR, "input[aria-invalid='false']").clear()
# driver.find_element(By.CSS_SELECTOR, "input[aria-invalid='false']").send_keys("pass11")
# time.sleep(3)


# Xpath
# absolute xpath -> absolute xpath starts from the root node
# relative xpath -> relative xpath can create from any parent node. It need not have to start from root node

# absolute xpath
driver.find_element(By.XPATH, "html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").clear()
driver.find_element(By.XPATH, "html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").send_keys("pass12")
time.sleep(2)

# relative xpath
driver.find_element(By.XPATH, "//input[@id = 'Password']").clear()
driver.find_element(By.XPATH, "//input[@id = 'Password']").send_keys("pass13")
time.sleep(2)

#OR
driver.find_element(By.XPATH, "//input[@value = 'admin']").clear()
driver.find_element(By.XPATH, "//input[@value = 'admin']").send_keys("pass14")
time.sleep(2)

#OR
driver.find_element(By.XPATH, "//input[@class = 'password']").clear()
driver.find_element(By.XPATH, "//input[@class = 'password']").send_keys("pass15")
time.sleep(2)

#OR
driver.find_element(By.XPATH, "//input[@type = 'password']").clear()
driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass16")
time.sleep(2)

#OR
driver.find_element(By.XPATH, "//input[@name = 'Password']").clear()
driver.find_element(By.XPATH, "//input[@name = 'Password']").send_keys("pass17")
time.sleep(2)

# for varying/changing field
driver.find_element(By.XPATH, "//*[starts-with(@id, 'Pass')]").clear()
driver.find_element(By.XPATH, "//*[starts-with(@id, 'Pass')]").send_keys("pass18")
time.sleep(2)

#OR  **Ends-with()(works only with xpath 2.0 version)
# driver.find_element(By.XPATH, "//*[ends-with(@id, 'word')]").clear()
# driver.find_element(By.XPATH, "//*[ends-with(@id, 'word')]").send_keys("pass19")
# time.sleep(2)

