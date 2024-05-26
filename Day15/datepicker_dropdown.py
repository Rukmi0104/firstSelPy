import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
driver.implicitly_wait(10)
dt1 = datetime.datetime(2025, 6, 11)
year = dt1.strftime("%Y")
month = dt1.strftime("%B")
d1 = dt1.strftime("%d").lstrip("0")
print(dt1)
#
sleep(2)
driver.find_element(By.ID, "datepicker2").click()

select_month = Select(driver.find_element(By.XPATH, "//select[@title='Change the month']"))
select_month.select_by_visible_text(month)
sleep(5)
select_year = Select(driver.find_element(By.XPATH, "//select[@title='Change the year']"))
select_year.select_by_visible_text(year)

driver.find_element(By.XPATH, f"//div[@class='datepick-month']/table/tbody/tr/td/a[text()= '{d1}']").click()

datepicker_data = driver.find_element(By.ID, "datepicker2").get_attribute("value")
if datepicker_data == dt1.strftime("%m/%d/%Y"):
    print(f"date entered successfully: {datepicker_data}")

sleep(10)
