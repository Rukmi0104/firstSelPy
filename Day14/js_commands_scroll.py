import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(10)
time.sleep(8)
driver.execute_script("window.scrollBy(0, 3000)")
time.sleep(3)
print(driver.execute_script("return window.pageYOffset;"))

# scroll by some condition
flag_ele = driver.find_element(By.XPATH, "//img[@alt= 'Flag of India']")
driver.execute_script("window.scrollBy")

