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

driver.get("https://money.rediff.com/gainers")

# get number of rows
rows = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr")
print(len(rows))

# get number of columns
columns = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td")
print(len(columns))

# get number of cells in table???
cells = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr/td")
print(len(cells))

# read data from 10th row and 4th column
data_1 = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/td[4]").text
print(data_1)

# printing all rows and column data
# for row in range(1, len(rows)+1):
#     for col in range(1, len(columns)+1):
#         data = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row}]/td[{col}]").text
#         print(data, "\t")


# read data based on condition. Read all data for company "Ganges Securities"
for r in range(1, len(rows)+1):
    row_data = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[1]").text
    if row_data == "Ganges Securities":
        for col in range(1, len(columns)+1):
            print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{col}]").text)
        break

