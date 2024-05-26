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

# scroll to Y 100 offset using ActionChains class
action = ActionChains(driver)
action.scroll_by_amount(0, 100)

#=========================
# webtable will always start with tag name table
# thead is for header, tbody is for table body
# mostly we inspect tbody to get table data, we do not inspect thead. If required we use thead to get column number and column heading
# print specific row or specific column
# in python if we have to use length then we use range function also

#===================================
# get column based on index
# header_ele = driver.find_elements(By.XPATH, "//table[@class='dataTable']/thead/tr/th")
#
# # here header_ele is a python list so we have to provide range starting with 0 (not with 1)
# header_col_len = len(header_ele)
# for index in range(header_col_len):
#     if header_ele[index].text == "Company":
#         company_index = index
#         company_column = index+1
# print(company_column)
# # here for td we are giving company_column as company_index+1 because company index is zero but it is first column in html.
#
# # using company index get all data from company column
# # company_list = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr/td[{company_column}]")
# # for company_data in company_list:
# #     print(company_data.text)
#
# #===================== get company name if current price is less than 2rs
# # get current price index based on header data.. similar to above company example
# for col_index in range(header_col_len):
#     if header_ele[col_index].text =="Current Price (Rs)":
#         current_price_index = col_index
#         current_price_column = col_index+1
# #---------------------------------
# # get company data whose current price is less than 2 rs.
# # collect row element
# row_ele = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr")
# #get length of rows
# row_len = len(row_ele)
# # iterate through rows to get current price
# for row in range(1, row_len+1):
#     each_row_data = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row}]/td[{current_price_column}]").text.replace(",", "")
#     # print(each_row_data)
#     # iterate though columns once we get current price and based on CP get company data
#     if float(each_row_data) <= 2:
#         company_below_2_rs = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row}]/td[{company_column}]").text
#         # print(company_below_2_rs)



#===================== get row data if based on Group. If Group is 'A' then print row detail
#Step1 --> get index of 'Group' column based on header element
    # get num of columns
header_ele1 = driver.find_elements(By.XPATH, "//table[@class='dataTable']/thead/tr/th")
len_header_ele1 = len(header_ele1)
    # now after getting total length, we can get index of 'Group' column as below

for grp_index in range(len_header_ele1):
    if header_ele1[grp_index].text == "Group":
        Group_index = grp_index
        Group_column_position = Group_index+1

    # based on group column index get all data in that column and iterate throught it
tot_row_1 = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr")
len_tot_row1 = len(tot_row_1)
table_col = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{Group_column_position}]/td")
table_col_len = len(table_col)
    # using this length iterate through rows and get Group data entry
for row1 in range(1, len_tot_row1+1):
    each_row_grp_data = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row1}]/td[{Group_column_position}]").text
    # print(each_row_grp_data)
    for col1 in range(1, table_col_len+1):
        if each_row_grp_data == "A":  # then -->  get entire row data
            row_new_data = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{row1}]/td[{col1}]").text
            print(row_new_data, end="\t")
    if each_row_grp_data == "A":
        print("\n")



