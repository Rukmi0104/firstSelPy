# hardcode can work for static webtable but it will not work for dynamic table where data keeps on changing


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
action.scroll_by_amount(0, 500).perform()

# get company index and based on index get column data in for rows
# step 1 get total number of columns using hearder element,with this we will get length of column
# for loop is for python list which starts with index 0
col_num = driver.find_elements(By.XPATH, "//table[@class= 'dataTable']/thead/tr/th")
col_len = len(col_num)  # from this we have total number of columns in table
print(col_len)

# step 2 get index of any 1 column ex.'Company' column
for col_ind in range(col_len):      # we are iterating through list so we are getting index starting with 0.
    if col_num[col_ind].text == "Company":
        company_index = col_ind

# print(company_index)
#
# # with the company index get all data of Company column
company_list = driver.find_elements(By.XPATH, f"//table[@class= 'dataTable']/tbody/tr/td[{company_index+1}]")
print(company_list)
for company_name in company_list:
    print(company_name.text)


# # get "Current Price (Rs)" column index using hearder data
# for col_indx in range(col_len):
#     if col_num[col_indx].text == "Current Price (Rs)":
#         cp_ind = col_indx
# print(cp_ind)
#
# # get total number of rows
# row_ele = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr")
# row_len = len(row_ele)
# print(row_len)
#
# ## this loop is for html index
#
# for r in range(1, row_len+1):
#     cur_prc = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{cp_ind+1}]").text.replace(",", "")
#     if float(cur_prc) <= 10:
#         print(f"company name is {company_name.text}, current price {cur_prc}")
#     else:
#        comp_name = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{company_index+1}]").text
#        print(f"{cur_prc} is greater than 1")






