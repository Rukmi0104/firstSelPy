
# shadow DOM is used by HTML developer to reuse the code
# if they want to used same code then create a shadow dom

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

######################################## single shadow dom
# driver.get("https://books-pwakit.appspot.com/")
#
# shadowroot_1 = driver.find_element(By.CSS_SELECTOR, "")
# driver.find_element(By.ID, "//ul[@class='results-base']/li[1]").click()

######################################## multiple shadow dom


driver.get("chrome://settings/downloads")
shadow_1 = driver.find_element(By.CSS_SELECTOR, "settings-ui").shadow_root
shadow_2 = shadow_1.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root
shadow_3 = shadow_2.find_element(By.CSS_SELECTOR, "settings-basic-page.cr-centered-card-container").shadow_root
shadow_4 = shadow_3.find_element(By.CSS_SELECTOR, "settings-downloads-page").shadow_root
shadow_5 = shadow_4.find_element(By.CSS_SELECTOR, "settings-toggle-button.hr").shadow_root
text_1 = shadow_5.find_element(By.CSS_SELECTOR, "div.label").text
print(text_1)
