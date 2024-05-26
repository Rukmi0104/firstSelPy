import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

### Frame is a website inside another website
# example. some website will use youtube video link on their website.
# So, youtube is a separate website which is embedded in another website. This is done with frames
# frames are nothing but embedding one website inside another website
# to find out the diff xpath for frames chropath will not work.
# So we have to create our own xpath based on knowledge and use it
serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
frame1_ele = driver.find_element(By.XPATH, "//frame[@src='frame_1.html']")
driver.switch_to.frame(frame1_ele)
driver.find_element(By.NAME, "mytext1").send_keys('frame1 search engine')
time.sleep(3)
driver.switch_to.default_content()

frame2_ele = driver.find_element(By.XPATH, "//frame[@src='frame_2.html']")
driver.switch_to.frame(frame2_ele)
driver.find_element(By.NAME, "mytext2").send_keys('frame2 search engine')
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
frame3_ele = driver.find_element(By.XPATH, "//frame[@src='frame_3.html']")
driver.switch_to.frame(frame3_ele)
time.sleep(3)
driver.find_element(By.NAME, "mytext3").send_keys('frame3 search engine')
time.sleep(3)

iframe_ele = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe_ele)
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()= 'Other:']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@class='Hvn9fb zHQkBf']").send_keys("hello")
time.sleep(2)

driver.switch_to.parent_frame()     # come out of inner frame, and focus will go to parent frame frame3
driver.find_element(By.NAME, "mytext3").clear()
driver.find_element(By.NAME, "mytext3").send_keys('frame3 search engine after clear')
time.sleep(5)

