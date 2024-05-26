from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class login_page:
    email_txt_id = "Email"
    password_txt_id = "Password"
    login_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_txt_id).clear()
        self.driver.find_element(By.ID, self.email_txt_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_txt_id).clear()
        self.driver.find_element(By.ID, self.password_txt_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()






