import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
# from hybrid_framework.utilities.custom_logger import log_logger_as_append
from hybrid_framework.utilities.custom_logger import log_logger_as_append

print(sys.path)
sys.path.append(r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA")
from hybrid_framework.pageObjects.login_page import login_page
from hybrid_framework.utilities.read_config import read_config_class

ss_folder = r"D:\\SeleniumPython\\Projects\\FITA\\pythonProject1_FITA\\hybrid_framework\\screenshots\\"


class Test_suite_login_001:
    # get_log = log_logger_as_append()
    get_log = log_logger_as_append()

    def test_case_verify_title_01(self, launch_browser_setup):
        driver = launch_browser_setup
        self.get_log.info("launched browser for test_case_verify_title_01")

        actual_title_01 = "Your store. Login"
        self.get_log.info("verify title for test_case_verify_title_01")
        if driver.title == actual_title_01:
            self.get_log.info("title matched.. test_case_verify_title_01 is passed")
            assert True

        else:
            self.get_log.info("title didnt match.. test_case_verify_title_01 is failed")
            driver.save_screenshot(ss_folder+"test_case_verify_title_01.png")
            assert False

    def test_case_do_login_verify_title_02(self, launch_browser_setup):
        driver = launch_browser_setup
        self.get_log.info("launched browser for test_case_do_login_verify_title_02")
        lp = login_page(driver)
        self.get_log.info("initiating login_page class")
        self.get_log.info("set email id")
        lp.setEmail(read_config_class.getEmail())
        self.get_log.info("set password")
        lp.setPassword(read_config_class.getPassword())
        self.get_log.info("click login")
        lp.clickLogin()
        self.get_log.info("logged in to NOP commerce successfully")
        time.sleep(3)
        actual_title_02 = "Dashboard / nopCommerce administration"
        if driver.title == actual_title_02:
            self.get_log.info("title matched.. test_case_do_login_verify_title_02 is passed")
            assert True

        else:
            self.get_log.info("title didnt match.. test_case_do_login_verify_title_02 is failed")
            driver.save_screenshot(ss_folder+"test_case_do_login_verify_title_02.png")
            assert False



