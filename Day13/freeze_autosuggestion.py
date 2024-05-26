# if you want to freeze autosuggestion or tooltip for getting xpath then we can
# freeze them and perform inspect element operation

# option1

# using direct option.. that is attribute given for element
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.google.com/")
driver.implicitly_wait(10)
# time.sleep(5)
# google_app_tooltip_ele = driver.find_element(By.XPATH, "//div[contains(text(), 'Google apps')]")
# print(google_app_tooltip_ele.text)


# time.sleep(2)
google_app_ele = driver.find_element(By.XPATH, "//a[@aria-label='Google apps']")
# time.sleep(2)
google_app_tooltip_ele = driver.find_element(By.XPATH, "//div[contains(text(), 'Google apps')]")
# time.sleep(2)
action = ActionChains(driver)
action.move_to_element(google_app_ele).perform()
time.sleep(4)

print(google_app_tooltip_ele.text)

time.sleep(4)


driver.get("https://demoqa.com/tool-tips")
driver.implicitly_wait(10)
# from event listener, remove properties, collect element and perform operation
hover_me_tooltip_ele = driver.find_element(By.XPATH, "//a[text()='You hovered over the Button']")
print(hover_me_tooltip_ele.text)
time.sleep(4)


