# cookies are nothing but data/ memory of that page

#. In login page Uname and password field data are auto-populated. These are populated from the cookies.
# cookies are actually memory management for the browser.
# all the history or all the data which we are giving in the page, it will show as suggestion box. whatever we search previously, it show in suggestion box.. it comes from cookies.
# secure and well maintained page will/should always allow to create/update/ delete the cookies
# so the delete, create, update cookies we can do with the automation and we can check if webpage is okay with the cookies.

# get the cookies

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

location = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\Day14"
serv_obj = Service(r"D:\SeleniumPython\Projects\FITA\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# if we know the exact cookie name and want to get it then we can execute below function.
# driver.get_cookie()


# if we dont know specific cookie name, then we can get all available cookies
print(driver.get_cookies())
# o/p -->
#[{'domain': 'admin-demo.nopcommerce.com', 'httpOnly': True, 'name': '.Nop.Antiforgery', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': 'CfDJ8IiSoo1ocrtFvurdsk63e1RTxKVYIGGh_1UAGQIhwnq2k37hNw1NIMVPaWlqVz8-oW8KR6JJP9JhjcBHa0MrzKXnWJ_lXLTvRd3bA__1rmjhPY3qgmXXFHaSlzx1_GnNBt1s0L-TZ8PxJmv6EVHXMs0'},
# {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1744652502, 'httpOnly': False, 'name': '.Nop.Culture', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c%3Den-US%7Cuic%3Den-US'},
# {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1744652502, 'httpOnly': True, 'name': '.Nop.Customer', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'b4ee3946-7ced-4e09-8058-7648c651669f'}]

# the correct/proper cookie will have name and value
# if we want to create the cookie then we should have correct name and value
