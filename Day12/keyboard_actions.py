# keyboard actions we use for autocomplete or autosuggestion
# for autocomplete there is no need to use ActionChains class, we can use driver object to perform keyboard operations

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://jqueryui.com/autocomplete/")

# locate frame
frame_ele = driver.find_element(By.TAG_NAME, "iframe")
# switch to frame
driver.switch_to.frame(frame_ele)

# locate element Tags and type text "a" using send key and select random element using arrow_down
# driver.find_element(By.ID, "tags").send_keys("a")
# time.sleep(2)
# driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
# time.sleep(2)
# # driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
# # time.sleep(2)
# driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)
# time.sleep(2)
# print(driver.find_element(By.ID, "tags").get_attribute("value"))

##################### selecting particular element using while loop#################

# driver.find_element(By.ID, "tags").send_keys("a")
# while True:
#     driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
#     get_input_text = driver.find_element(By.ID, "tags").get_attribute("value")
#     if get_input_text == "Java":
#         driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)
#         break
#     time.sleep(4)
# print(driver.find_element(By.ID, "tags").get_attribute("value"))
# time.sleep(4)

##################### selecting particular element using for loop#################

driver.find_element(By.ID, "tags").send_keys("a")

for i in range(30):
    get_input_text = driver.find_element(By.ID, "tags").get_attribute("value")
    if get_input_text == "Java":
        driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)
    else:
        driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
print(driver.find_element(By.ID, "tags").get_attribute("value"))
time.sleep(4)




