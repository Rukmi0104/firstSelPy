import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.myntra.com/tops")

driver.find_element(By.XPATH, "//ul[@class='results-base']/li[1]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[2]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[3]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[4]").click()
time.sleep(10)

win_session_id = driver.window_handles
print(win_session_id)
driver.switch_to.window(win_session_id[3])

# for w in win_session_id[1:]:
#     driver.switch_to.window(w)
#     print(driver.find_element(By.XPATH, "//span[@class='pdp-price']/strong").text)
#     driver.find_element(By.XPATH, "//div[text()='ADD TO BAG']").click()
#     time.sleep(2)




