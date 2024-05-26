import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
#  the letter 'r' preceding a string signifies a 'Raw String'. This instructs the Python interpreter to interpret
#  backslashes in the string literally, rather than as escape characters, which is the default behavior

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Type1-> text alert -->  which gives only some information and we have to accept the alert
wait.until(ec.presence_of_element_located((By.XPATH, "//button[text()= 'Click for JS Alert']")))
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()= 'Click for JS Alert']").click()
text_alert = driver.switch_to.alert
text_alert.accept()

# Type2 -> confirmation alert which gives option to accept or reject/dismiss
wait.until(ec.presence_of_element_located((By.XPATH, "//button[text()= 'Click for JS Confirm']")))
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()= 'Click for JS Confirm']").click()
confirm_alert = driver.switch_to.alert
time.sleep(2)
confirm_alert.accept()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()= 'Click for JS Confirm']").click()
time.sleep(2)
confirm_alert.dismiss()
time.sleep(2)

# Type3 -> input/prompt alert. after providing some input we can accepts or reject the alert
wait.until(ec.presence_of_element_located((By.XPATH, "//button[text()= 'Click for JS Prompt']")))

driver.find_element(By.XPATH, "//button[text()= 'Click for JS Prompt']").click()
input_alert = driver.switch_to.alert
time.sleep(2)
input_alert.send_keys("input text in alert")
time.sleep(5)
print(input_alert.text)
input_alert.accept()
time.sleep(2)


driver.find_element(By.XPATH, "//button[text()= 'Click for JS Prompt']").click()
time.sleep(3)
input_alert.dismiss()
time.sleep(2)

