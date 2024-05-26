from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

# launch website
driver.get("https://money.rediff.com/gainers")
sleep(3)

# scroll to Y 100 offset using ActionChains class
action = ActionChains(driver)
action.scroll_by_amount(0, 100)

# get total number of rows in table body
row_nums = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr")
total_row_nums = len(row_nums)
print(total_row_nums)

# # get total number of cells in table body
# cell_nums = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr/td")
# total_cell_nums = len(cell_nums)
# print(total_cell_nums)

# get total number of columns in table using tbody xpath
col_nums_td = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr[1]/td")
total_col_nums_td = len(col_nums_td)
print(total_col_nums_td)

# get total number of columns in table using thead xpath
col_nums_th = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/thead/tr/th")
total_col_nums_th = len(col_nums_th)
print(total_col_nums_th)

# # get first row company data
# row1 = driver.find_element(By.XPATH, "//table[@class= 'dataTable']/tbody/tr[1]").text
# print(row1)

# # get first column data. Example "company" is the first column in table, so all data in company column will be shown.
# company_data = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr/td[1]")
# print(company_data)
# for company in company_data:
#     print(company.text)


# # get all row data in a table
# rows = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr")
# for row in rows:
#     print(row.text)
#
# # get all columns data in table
# cols = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr/td")
# for col in cols:
#     print(col.text)
#
#
# # get data from 2nd row and 3rd column
# row2_col3 = driver.find_element(By.XPATH, "//table[@class= 'dataTable']/tbody/tr[2]/td[3]").text
# time.sleep(3)
# print(row2_col3)

# get table data based on current price. If CP is less than 2 rs then show table data

        # step11:
# get rows deatil using current price column condition
empty_list = []
for r in range(1, total_row_nums+1):
    row_data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{r}]/td[4]").text.replace(",", "")
    empty_list.append(row_data)
    for col in range(1, total_col_nums_td+1):
        if float(row_data) <=2:
            row_detail = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{r}]/td[{col}]").text
            # empty_list.append(r)       # not working
            print(row_detail)
    break
print(empty_list)



