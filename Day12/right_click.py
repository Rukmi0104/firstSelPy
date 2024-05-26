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

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
action = ActionChains(driver)
right_click_element = driver.find_element(By.XPATH, "//span[text()= 'right click me']")
action.context_click(right_click_element).perform()
option_clk_sub_element = driver.find_element(By.XPATH, "//span[text()= 'Copy']")
action.move_to_element(option_clk_sub_element).click().perform()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()


