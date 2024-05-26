from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

# initiate ActionChain class
action = ActionChains(driver)
# collect the element on which double click should be performed
double_clk_ele = driver.find_element(By.XPATH, "//button[text()= 'Double-Click Me To See Alert']")
# perform double click using ActionChains class and double_click method
action.double_click(double_clk_ele).click().perform()

# accept alert
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
