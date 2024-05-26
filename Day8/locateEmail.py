# from https://admin-demo.nopcommerce.com/ login page locate email text field using different locators
import time

# normal locators -> id, name, classname, tag, link text and partial link text
# Custom locators -> css and xpath

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

# locate elements using normal locators -> id, name, classname, tag, link text and partial link text
# Locate email by id
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("ruk1")
time.sleep(3)

# Locate email by name
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("ruk2")
time.sleep(3)

# locate element by class name
driver.find_element(By.CLASS_NAME, "email").clear()
driver.find_element(By.CLASS_NAME, "email").send_keys("ruk3")
time.sleep(3)

##########################
# locate element by tag name
# driver.find_element(By.TAG_NAME, "input").clear()
# driver.find_element(By.TAG_NAME, "input").send_keys("ruk4")
# time.sleep(3)
    # this code will throw "selenium.common.exceptions.InvalidElementStateException:
# Message: invalid element state" as there are multiple elements with tag name "input".
# Everytime we have to give unique locator to identify the element.


##########################
# locate element by link text
# driver.find_element(By.LINK_TEXT, "")   # there is no link text in description, so we can not use this locator??
# time.sleep(3)

# locate element by partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT, "")   #there is no link text in description, so we can not use this locator?
# time.sleep(3)

# Locate email using Custom locators -> css and xpath
#CSS
#tag#id
#tag.classname
#tag[attribute= value]

driver.find_element(By.CSS_SELECTOR, "input#Email").clear()
driver.find_element(By.CSS_SELECTOR, "input#Email").send_keys("ruk5")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input.email").clear()
driver.find_element(By.CSS_SELECTOR, "input.email").send_keys("ruk6")
time.sleep(2)


driver.find_element(By.CSS_SELECTOR, "input[data-val-email= 'Wrong email']").clear()
driver.find_element(By.CSS_SELECTOR, "input[data-val-email= 'Wrong email']").send_keys("ruk7")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[data-val-required= 'Please enter your email']").clear()
driver.find_element(By.CSS_SELECTOR, "input[data-val-required= 'Please enter your email']").send_keys("ruk7")
time.sleep(2)

# Xpath
# absolute xpath -> absolute xpath starts from the root node
# relative xpath -> relative xpath starts with "//tagname" or "//*". It need not have to start from root node

# absolute xpath
driver.find_element(By.XPATH, "html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").clear()
driver.find_element(By.XPATH, "html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").send_keys("ruk8")
time.sleep(2)


# relative xpath
driver.find_element(By.XPATH, "//input[@id = 'Email']").clear()
driver.find_element(By.XPATH, "//input[@id = 'Email']").send_keys("ruk9")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//input[@class = 'email']").clear()
driver.find_element(By.XPATH, "//input[@class = 'email']").send_keys("ruk10")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//input[@name = 'Email']").clear()
driver.find_element(By.XPATH, "//input[@name = 'Email']").send_keys("ruk11")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//input[@type = 'email']").clear()
driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("ruk12")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//input[@value = 'admin@yourstore.com']").clear()
driver.find_element(By.XPATH, "//input[@value = 'admin@yourstore.com']").send_keys("ruk13")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//input[@class = 'email' and @id = 'Email']").clear()
driver.find_element(By.XPATH, "//input[@class = 'email' and @id = 'Email']").send_keys("ruk14")
time.sleep(2)


# OR
driver.find_element(By.XPATH, "//input[@class = 'email' or value = 'admin@yourstore.com']").clear()
driver.find_element(By.XPATH, "//input[@class = 'email' or value = 'admin@yourstore.com']").send_keys("ruk15")
time.sleep(2)


# OR
driver.find_element(By.XPATH, "//*[contains(@id, 'Email')]").clear()
driver.find_element(By.XPATH, "//*[contains(@id, 'Email')]").send_keys("ruk16")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//*[contains(@data-val-email, 'Wrong email')]").clear()
driver.find_element(By.XPATH, "//*[contains(@data-val-email, 'Wrong email')]").send_keys("ruk17")
time.sleep(2)

# OR
driver.find_element(By.XPATH, "//*[contains(@data-val-required, 'Please enter your email')]").clear()
driver.find_element(By.XPATH, "//*[contains(@data-val-required, 'Please enter your email')]").send_keys("ruk18")
time.sleep(2)


# OR
# text() will not work as there is no text available for email field?????
# "//tagName[contains(text(), 'value')"]. this will work on visible text.
# Search for all results which contains the input value
# example.
# driver.find_element(By.XPATH, "//*[contains(text(), 'email')]").clear()
# driver.find_element(By.XPATH, "//*[contains(text(), 'email')]").send_keys("ruk18")
# time.sleep(2)

#OR using inner text -> this is not working as there is no inner text for email field????
# "//tagName[text()= 'inner text available between > <']". Ex. >Email<.
# Search for exact matching value given in the input value
# driver.find_element(By.XPATH, "//input[text()= 'Email']").clear()
# driver.find_element(By.XPATH, "//input[text()= 'Email']").send_keys("ruk19")
# time.sleep(2)

# //tagname[contains(text((), 'value of text')] and //tagname[text()= 'value of text']
# both options will work for link text and for normal text visible on screen.
# only difference is with first option we can search all possible result which contains the given value.
# and with 2nd option we can search exact matching value only.
# so, usually for link text we can use contains(text()) to search related text. And for normal text we use text()

# OR
# for varying/changing field
driver.find_element(By.XPATH, "//*[starts-with(@id, 'Email')]").clear()
driver.find_element(By.XPATH, "//*[starts-with(@id, 'Email')]").send_keys("ruk20")
time.sleep(2)




