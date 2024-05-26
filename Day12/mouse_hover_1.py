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

driver.get("https://www.geeksforgeeks.org/")

# initiate action class and give driver object
action = ActionChains(driver)

################### option1 ################################
# get the xpath of the elements for which navigation and click is needed and save in a variable
course_elem = driver.find_element(By.XPATH, "//span[text() = 'Courses']")
working_prof_elem = driver.find_element(By.XPATH, "//span[text() = 'For Working Professionals']")
devops_eng_elem = driver.find_element(By.XPATH, "//a[text() = 'DevOps Engineering (LIVE)']")

# perform navigation
action.move_to_element(course_elem).perform()
action.move_to_element(working_prof_elem).perform()
# perform click
action.move_to_element(devops_eng_elem).click().perform()
print(driver.title)

################### option1 ################################
# we can perform above operations using move_to_element in single line

# action.move_to_element(course_elem).move_to_element(working_prof_elem).move_to_element(devops_eng_elem).click().perform()
# time.sleep(4)
# print(driver.title)




