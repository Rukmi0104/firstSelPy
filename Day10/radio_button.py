import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_ojb)
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()

driver.find_element(By.XPATH, "//ul[@role = 'menu']/li[4]/a/p[contains(text(), 'Customers')]").click()

driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']/i/following-sibling::p").click()

driver.find_element(By.XPATH, "//i[@class = 'fas fa-plus-square']").click()


# select Gender
def gen(gender):
    if gender == "Male":
        driver.find_element(By.CSS_SELECTOR, "input#Gender_Male").click()
    elif gender == "Female":
        driver.find_element(By.CSS_SELECTOR, "input#Gender_Female").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "input#Gender_Male").click()


gen("Female")



