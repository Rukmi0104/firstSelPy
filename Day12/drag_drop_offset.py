import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

action = ActionChains(driver)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
time.sleep(2)
# collect the elements
l_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
r_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

# check current offset position
print(l_slider.location)
print(r_slider.location)

# move from left to right in positive direction of x axis
action.drag_and_drop_by_offset(l_slider, 100, 0).perform()
# move from right to left in negative direction of x axis
action.drag_and_drop_by_offset(r_slider, -100, 0).perform()
# check offset position after drag and drop
print(l_slider.location)
print(r_slider.location)
time.sleep(3)
