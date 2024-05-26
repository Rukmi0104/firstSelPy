# if we want to download file in specified path, then need to give preference before initiating driver object
#
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

location = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\Day14"
# serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\msedgedriver.exe")
preferences = {"download.default_directory": location}
ff_op = webdriver.FirefoxOptions()
ff_op.set_preference("browser.download.folderList", 0)  # 0-desktop,1-downloadfolder,2-desiredloc
ff_op.set_preference("browser.download.dir", location)
driver = webdriver.Firefox(options=ff_op)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()

# Navigate to products # dropdown type1 without select tag. With Ul or Li tag
driver.find_element(By.XPATH, "//ul[@role= 'menu']/li/a/p[contains(text(), 'Catalog')]").click()
sleep(4)
driver.find_element(By.XPATH, "//ul[@role= 'menu']/li[2]/ul/li/a/p[contains(text(), 'Products')]").click()

# download excel in default location
sleep(3)
driver.find_element(By.CSS_SELECTOR, "button.dropdown-toggle").click()
driver.find_element(By.XPATH, "//button[@name = 'exportexcel-all']").click()

time.sleep(20)



