import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.geeksforgeeks.org/")
print(driver.window_handles)        # this will give session is for parent window
time.sleep(4)
driver.find_element(By.XPATH, "//div[2]/div/div/a/img").click()
driver.find_element(By.XPATH, "//div[2]/div/div/a/img").click()
driver.find_element(By.XPATH, "//div[2]/div/div/a/img").click()
print(driver.title)     # since we do not switch to community window, title is shown for parent window
# driver.close()  # -> parent window is closed as driver focus is on parent window.

win_list = driver.window_handles    # this will give session id list of all windows that are opened
print(win_list)

# getting focus on child window
for w in win_list[1:]:
    driver.switch_to.window(w)
    print(f" window session id is {w} and title is '{driver.title}'")

print("------with parent window session is")
# parent window will also include
for win in win_list:
    driver.switch_to.window(win)
    print(f" window session id is {win} and title is '{driver.title}'")







