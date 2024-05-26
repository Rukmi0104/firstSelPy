import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

## launch chrome driver
service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_ojb)
driver.get("https://admin-demo.nopcommerce.com/")
time.sleep(3)


## launch edge driver
# service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\msedgedriver.exe")
# driver = webdriver.Edge(service=service_ojb)
# driver.get("https://www.google.com/")
# time.sleep(3)


## launch firefox driver
# service_ojb = Service(r"D:\SeleniumPython\Projects\FITA\geckodriver.exe")
# driver = webdriver.Firefox(service=service_ojb)
# driver.get("https://admin-demo.nopcommerce.com/")
# time.sleep(3)

actual_title = driver.title
print(actual_title)
driver.maximize_window()
time.sleep(2)
driver.refresh()
time.sleep(2)
print(driver.current_url)
print(driver.page_source)
driver.back()
title_after_navigatingBack = driver.title
print(title_after_navigatingBack)

########### browser commands ############

driver.close()
# -> closes only one browser. that means it is driver focused.
# The tab/window where browser is active currently that tab/window will be closed.


driver.quit()
# closes the entire sessions/tab/window and quit the browsers
# ensures backend process will be killed.

########### conditional commands ############

