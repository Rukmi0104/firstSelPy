import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from hybrid_framework.utilities.read_config import read_config_class


@pytest.fixture()
def launch_browser_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service(
            r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service(
            r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service(
            r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service(
            r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    driver.get(read_config_class.getURL())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

#
# def pytest_configuration(config):
#     config._metadata={
#         "tester": "Rukmini",
#         "project": "nop commerce",
#     }
#

