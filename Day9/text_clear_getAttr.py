import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.geeksforgeeks.org/")

# below code is giving blank value, how to get blinking text in input field
text1 = driver.find_element(By.CSS_SELECTOR, "input.ant-input").get_attribute('value')
time.sleep(1)
print(text1)
# text2 = driver.find_element(By.CSS_SELECTOR, "input.ant-input").text
# time.sleep(1)
# print(text2)

driver.find_element(By.CSS_SELECTOR, "input.ant-input").send_keys("hello geeks for geeks")

input_text = driver.find_element(By.CSS_SELECTOR, "input.ant-input").get_attribute('value')
print(input_text)

# get text for button
txt_search = driver.find_element(By.CSS_SELECTOR, "button.ant-input-search-button").text
print(txt_search)

# get text for anchor tag a
txt_community = driver.find_element(By.XPATH, "//a[@href='https://www.geeksforgeeks.org/community/?ref=homepage']").text
print(txt_community)

driver.find_element(By.CSS_SELECTOR, "input.ant-input").clear()

input_text_after_clear = driver.find_element(By.CSS_SELECTOR, "input.ant-input").get_attribute('value')
print(input_text_after_clear)

