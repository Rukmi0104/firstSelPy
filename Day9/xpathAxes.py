import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
time.sleep(3)

# xpath axes are used when there is other parameters to locate the element.

# consider below as self node
# <a href="//money.rediff.com/companies/innocorp/12200078" xpath="1"> Innocorp </a>

# locate self node
# val1 = driver.find_element(By.XPATH, "//a[contains(text(), 'Tata Consultancy')]").get_attribute('href')
# print(val1)
#
# # Locate parent node
# val2 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td").get_attribute('href')
# print(val2)
#
# # Locate ancestor node
# val3 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/ancestor::td").get_attribute('href')
# print(val3)
#
# # Locate following node
# val4 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/following::td").text
# print(val4)
#
# # Locate parent and following nodes
# val5 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td/following::td").text
# print(val5)

#get ancestor of self node
# val6 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td/ancestor::tr").text
# print(val6)
#######Observation#### output of val4 and val5 is same. so what we are using 2 diff ways?

#get all preceding rows
# val7 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td/preceding::tr").text
# print(val7)


#get first preceding row
# val7 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td/preceding::tr[1]").text
# print(val7)

# get first descendant
# currently there is descendant for self node a so will not get any out put
# val8 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/descendant::tr").text
# print(val8)
#
# val9 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/descendant::td").text
# print(val9)

#following sibling after reaching parent node
# val10 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td/following-sibling::td").text
# print(val10)
#
#
# # following sibling after reaching ancestor
# val11 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/ancestor::td/following-sibling::td").text
# print(val11)

# what is difference between val10 and val11 xpath

#preceding sibling after reaching parent node ############ NOT WORKING ######
# val10 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/parent::td/preceding-sibling::td").text
# print(val10)

# preceding sibling after reaching ancestor ############ NOT WORKING ######
# val11 = driver.find_element(By.XPATH, "//a[contains(text(),'Tata Consultancy')]/ancestor::td/preceding-sibling::td").text
# print(val11)

# find element with multiple matching web element
# if multiple elements are matching then it will click on first element
# val12 = driver.find_element(By.XPATH,"//tbody/tr/td/a").text
# print(f"val12 is {val12}")
# driver.find_element(By.XPATH, "//tbody/tr/td/a").click()
# time.sleep(5)
# print(driver.title)

######### find elements #############
# in general find_elements gives list of objects for matching elements
# print(driver.find_elements(By.XPATH, "//a[text()= 'Funds of Funds']"))
# so, we can save the element and use for loop to perform operation

#single matching web element
# elem = driver.find_elements(By.XPATH, "//a[text()= 'Funds of Funds']")
# for i in elem:
#     i.click()
#     print(driver.title)
# driver.back()
#
#
# print(driver.title)
# driver.back()
# time.sleep(5)
# print(driver.title)

# multiple matching web element
# elem1 = driver.find_elements(By.XPATH, "//tbody/tr/td/a")
# for j in elem1:
#     print(j.text)            # unable to get first element with indexing


# find_elements with invalid xpath:
# it will not throw any error. If we try to print it, then empty list will be given. SO if we want to handle error,
# then also we can go wth fine_elements
ele = driver.find_elements(By.XPATH, "//asdasdadad")
print(ele)

# find_elements with send_keys throw error --> AttributeError: 'list' object has no attribute 'send_keys'
# driver.find_elements(By.XPATH, "//asdasdadad").send_keys("abc")



