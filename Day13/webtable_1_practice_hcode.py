import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://money.rediff.com/gainers")

action = ActionChains(driver)
action.scroll_by_amount(0, 2000).perform()
# time.sleep(4)

############################################
# get number of columns in a table
# option 1 using column headers
col_num_1 = driver.find_elements(By.XPATH, "//thead/tr/th")
col_len = len(col_num_1)
print(col_len)

# option 2 using columns in tbody
col_num_2 = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td")
col_len_2 = len(col_num_2)
print(col_len_2)

############################################
# get number of rows in a table
# option 1 including header row
# how to get???


# option 2 excluding header row
rows_without_header = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr")
row_len = len(rows_without_header)
print(row_len)

############################################
# Option 1 get total number of cells in table using len function
cell_num = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/tbody/tr/td")
cell_len = len(cell_num)
print(cell_len)


# option 2 get total number of cells in table using * operator

def table_cells(col_num, row_num):
    total_cells = col_num * row_num
    return total_cells


total_cells = table_cells(col_len, row_len)
print(f"total number of cells in a table are {total_cells}")

############################################
# # printing all table body data using for loop
# # apply for loop on collected rows and columns lengths in a datatable
#
# for r in range(1, row_len + 1):
#     for c in range(1, col_len+1):
#         data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{r}]/td[{c}]").text
#         print(data)

############################################
# # get data for only one row using some condition
# # Read row data when company is 'Nagpur Power'
#
# for r in range(1, row_len+1):
#     row_data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{r}]/td[1]").text
#     if row_data == "Flex Foods":
#         for c in range(1, col_len+1):
#             matching_row_data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{r}]/td[{c}]").text
#             # print(matching_row_data)
#
#             # get data in single line after sapce
#             print(driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{r}]/td[{c}]").text, end="\t")
#         break


############################################
# # get data for only one row using some condition
# # Read row data when company is 'Nagpur Power'
# # changing for and if loop conditions
# for rw in range(1, row_len+1):
#     row_data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{rw}]/td[1]").text
#     for cl in range(1, col_len+1):
#         if row_data == "Billwin Industries L":
#             row_detail = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{rw}]/td[{cl}]").text
#             print(row_detail)

############################################
# # get info of all stocks whose Current price is less than 1
#
for row_price in range(1, row_len+1):
    price_data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{row_price}]/td[4]").text.replace(",", "")
    if float(price_data) <= 1:
        for coll in range(1, col_len+1):
            stocks_data = driver.find_element(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr[{row_price}]/td[{coll}]").text
            print(stocks_data)





