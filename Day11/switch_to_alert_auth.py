import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#  the letter 'r' preceding a string signifies a 'Raw String'. This instructs the Python interpreter to interpret
#  backslashes in the string literally, rather than as escape characters, which is the default behavior

################
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# ## ################### invalid approach
# auth_alt = driver.switch_to.alert
# print(auth_alt.text)
# auth_alt.send_keys("admin")
# auth_alt.send_keys("admin")
# auth_alt.accept()

# ## option1 : auth pop-up can be handled by providing id and pass in ULR directly
# # example: https://username:password@url
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
# time.sleep(2)

# but sometimes this approach will not work
# so option 2 can be used. Auth pop-up can be handled using autoit approach
# Using autoit approach we can mimic the keyboard functionality.
# we need to install pyautoit, then we can use keyboard functions to operate on auth pop-up

## option2

import autoit
driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
autoit.win_wait_active("", 10)
autoit.send("admin{TAB}")
autoit.send("admin{TAB}")
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(4)

## below code is not working
after_login_title = driver.title
print(after_login_title)



