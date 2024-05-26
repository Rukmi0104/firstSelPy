# any page starting with anchor tag a is link

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

# initialize browser
service_object = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# open http://www.deadlinkcity.com/
driver.get("http://www.deadlinkcity.com/")

# # get all links from http://www.deadlinkcity.com/
#
# all_links = driver.find_elements(By.TAG_NAME, "a")
# for link in all_links:
#     print(link.get_attribute("href"))

#############################
# # get the status code of each link/url.
# # to get the status code we need to import module name 'requests'
# all_links = driver.find_elements(By.TAG_NAME, "a")
# for link in all_links:
#     url = link.get_attribute("href")
#     status = requests.get(url)
#     print(f"status code for {url} is {status.status_code}")

##############################
# # check valid and invalid url
# all_links = driver.find_elements(By.TAG_NAME, "a")
# for link in all_links:
#     url = link.get_attribute("href")
#     status = requests.get(url)
#     if int(status.status_code) >= 299:
#         print(f"status code is {status.status_code} and its invalid url {url}")
#     else:
#         print(f"status code is {status.status_code} and its valid url {url}")


#########################################
# handle exception for the links whose status code is not exist
all_links = driver.find_elements(By.TAG_NAME, "a")
for link in all_links:
    url = link.get_attribute("href")
    # print(status)
    try:
        status = requests.get(url)
        if int(status.status_code) >= 299:
            print(f"url {url} have invalid status code {status.status_code}")
        else:
            print(f"url {url} have valid status code {status.status_code}")
    except:
        print(f"{url} have no status code")

# usually in project we will get valid code only...

# invalid code we will have to check in case of developers have given only the links.
# If we click on the links it will not redirect to any pages or anything. It will barely a link.
# Those links developer will provide because in future some development is going to happen on that link.
# So we can handle those links using above scenarios.
# such links we call as reserved links.
