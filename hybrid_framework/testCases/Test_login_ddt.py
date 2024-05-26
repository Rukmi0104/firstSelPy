import pytest

from hybrid_framework.pageObjects.login_page import login_page
from hybrid_framework.utilities.xl_utilities import *
from hybrid_framework.testData.load_login_data_from_excel import load_xl_login_data
from hybrid_framework.utilities.custom_logger import log_logger_as_append

xl_path = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\hybrid_framework\testData\login_test_data.xlsx"


class Test_suite_login_001_ddt:
    get_log = log_logger_as_append()

    @pytest.mark.parametrize("email, passwd, expected", load_xl_login_data(xl_path, "Sheet1"))
    def test_case_do_login_verify_title_02_ddt(self, launch_browser_setup, email, passwd, expected):
        self.driver = launch_browser_setup
        lp = login_page(self.driver)
        lp.setEmail(email)
        lp.setPassword(passwd)
        lp.clickLogin()

        if expected == "pass":
            if self.driver.title == "Dashboard / nopCommerce administration":
                self.get_log.info("login to NOP site is successful, test_case_do_login_verify_title_02_ddt is passed")
            else:
                self.get_log.info("login to NOP site is not successful, test_case_do_login_verify_title_02_ddt is failed")
        elif expected == "fail":
            if self.driver.title != "Dashboard / nopCommerce administration":
                self.get_log.info("login to NOP site is not successful, test_case_do_login_verify_title_02_ddt is passed")








