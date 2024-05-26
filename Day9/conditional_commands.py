import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

## launch chrome driver
service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_ojb)
# driver.get("https://www.linkedin.com/learning-login")
driver.maximize_window()
time.sleep(3)

# print(driver.find_element(By.ID, 'auth-id-button').is_displayed())
# # this will return true as element is available in browser page
#
# print(driver.find_element(By.ID, 'auth-id-button').is_enabled())
# # this will return false as element is not enabled on the browser page
#
# driver.find_element(By.ID, 'auth-id-input').send_keys('abcds')
#
# print(driver.find_element(By.ID, 'auth-id-button').is_enabled())
# # this will return true as element is enabled after entering email
#
# print(driver.find_element(By.ID, 'auth-id-button').is_selected())
# this will return false as there is no option to select deselect the element.
# is selected will work on checkbox and radio buttons as below

# time.sleep(3)
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
# time.sleep(1)

# print(driver.find_element(By.CSS_SELECTOR, 'input#RememberMe').is_selected())
# # this will return false as RememberMe button is not checked.
#
# driver.find_element(By.CSS_SELECTOR, 'input#RememberMe').click()
#
# print(driver.find_element(By.CSS_SELECTOR, 'input#RememberMe').is_selected())
# # this will return true as RememberMe button is clicked ands checked.

### is selected will not work for input tagname 'li'. It will work for tagname 'input'
# example of li tag is as below

# time.sleep(1)
# driver.get("https://www.makemytrip.com/")
# time.sleep(5)
# HOW TO CLOSE IMAGE ON WEBPAGE https://www.makemytrip.com/ with below locator it is not working
# driver.find_element(By.CSS_SELECTOR, "a#webklipper-publisher-widget-container-notification-close-div").click()

# print(driver.find_element(By.XPATH, "//li[contains(text(), 'Round Trip')]").is_selected())
#
# driver.find_element(By.XPATH, "//li[contains(text(), 'Round Trip')]").click()
# print(driver.find_element(By.XPATH, "//li[contains(text(), 'Round Trip')]").is_selected())

driver.get("https://www.facebook.com/signup")

# print(driver.find_element(By.XPATH, '//label[text()= "Female"]').is_selected())
#
# driver.find_element(By.XPATH, '//label[text()= "Female"]').click()
# print(driver.find_element(By.XPATH, '//label[text()= "Female"]').is_selected())
# IN THE PREVIOUS STEP RADIO BUTTON "FEMALE" IS CLICKED, STILL IS_SELECTED RESULT IS FALSE

# --> Answer: use below locator with input tag. is_selected work only with input tag. So below code will work
print(driver.find_element(By.XPATH, '//label[text()= "Female"]/following-sibling::input').is_selected())
driver.find_element(By.XPATH, '//label[text()= "Female"]/following-sibling::input').click()
print(driver.find_element(By.XPATH, '//label[text()= "Female"]/following-sibling::input').is_selected())


