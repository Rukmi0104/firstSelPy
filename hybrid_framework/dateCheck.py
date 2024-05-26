import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
sleep(5)


def func1(y, m, d):
    dt1 = datetime.datetime(y, m, d)
    # print(dt1.strftime("%m/%d/%Y"))
    month = dt1.strftime("%B")
    year = dt1.strftime("%Y")
    d1 = dt1.strftime("%d").lstrip("0")  # with zero padding

    driver.find_element(By.ID, "datepicker2").click()
    sleep(5)
    month_drpdown = Select(driver.find_element(By.XPATH, "//select[@title='Change the month']"))
    month_drpdown.select_by_visible_text(month)
    sleep(5)
    year_drpdown = Select(driver.find_element(By.XPATH, "//select[@title='Change the year']"))
    year_drpdown.select_by_visible_text(year)
    sleep(5)
    driver.find_element(By.XPATH, f"//div[@class='datepick-month']/table/tbody/tr/td/a[text()='{d1}']").click()

    if driver.find_element(By.ID, "datepicker2").get_attribute("value") == dt1.strftime("%m/%d/%Y"):
        print("date entered successfully ", driver.find_element(By.ID, "datepicker2").get_attribute("value"))

    sleep(10)


func1(2025, 12, 22)
