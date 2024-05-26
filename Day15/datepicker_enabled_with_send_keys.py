''' if tagname is 'input' and datepicker text box is enabled then we can use send_keys() to enter the date.
In send_keys we have to give correct format then only it will work

datepicker which have dropdown for month and year, we can use Select() class

there is module in python 'datetime' -> purpose  of datetime is if we are giving any numerical equivalent of day, date or year, it wwill convert into aplhabetical
equivalent. Or alphabetical equivalent to numeric equivalent

%p  Locale’s equivalent of either AM or PM.
%M  Minute as a zero-padded decimal number. 00, 01, …, 59
%S  Second as a zero-padded decimal number. 00, 01, …, 59
%m  Month as a zero-padded decimal number. 01, 02, …, 12
%B  Month as locale’s full name.    January, February, …, December (en_US);
Januar, Februar, …, Dezember (de_DE)


'''

# option1 using send_keys()

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

# few basic functions

# get current date and time-->
print(datetime.datetime.now())      # output --> 2024-04-21 20:24:52.996697

# format date and time
dt1 = datetime.datetime.now()

# there is a format to give date in datetime strftime as below
# (year, month, date, hour, min, sec, milisecond)
print(dt1.strftime("%y %B %d %H %M %S %f %p"))      # strftime is a class used to format date and time in required structure

print(dt1)      # if we dont give nay format it takes default format

# get date and time for particular month and date
# lets take 1 date and do the formatting Ex.
# enter date and time according to the standard format as below. Also month is without zero padding

# dt2 = datetime.datetime(2024, 4, 11, 12, 23, 453322)

# take any date and pass it in default datetime class
dt3 = datetime.datetime(2024, 5, 22)
# since the required date is in the MM/DD/YYYY format and default date is in the YYYY, M, DD format,
# we have change format of default date as below

required_date = dt3.strftime("%m/%d/%Y")

driver.find_element(By.ID, "datepicker2").clear()
sleep(2)
driver.find_element(By.ID, "datepicker2").send_keys(required_date)
sleep(2)
datepicker_data = driver.find_element(By.ID, "datepicker2").get_attribute("value")

if required_date == datepicker_data:
    print(f"date entered successfully : {datepicker_data}")

sleep(2)
