import datetime
import random
import string
from time import sleep

import pytest

from hybrid_framework.testCases.Test_login import login_page
from hybrid_framework.utilities.read_config import read_config_class
from hybrid_framework.pageObjects.add_customer_page import add_customer_page
from hybrid_framework.utilities.custom_logger import log_logger_as_append


class Test_add_customer_003:
    log_logger = log_logger_as_append()

    @pytest.mark.regression
    def test_add_save_customer(self, launch_browser_setup):
        self.driver = launch_browser_setup
        lp = login_page(self.driver)
        lp.setEmail(read_config_class.getEmail())
        lp.setPassword(read_config_class.getPassword())
        lp.clickLogin()

        ac = add_customer_page(self.driver)
        ac.navigateCustomerPage()
        ac.clickAddNewButton()

        email = []
        for i in range(8):
            email.append(random.choice(string.ascii_letters + string.digits))

        ac.setEmail("".join(email)+"@gmail.com")
        ac.setPassword("1234")
        ac.setFirstName("myfisrtname")
        ac.setLastName("mylastname")
        ac.setGender("Male")
        # ac.setDOB("06-06-2024")
        ac.setCompanyName("abcabcc")
        ac.clickTaxExempt()
        sleep(3)
        ac.setNewsLetter("Your store name")
        sleep(2)
        ac.setCustomerRole("Administrators")
        # sleep(2)
        ac.select_vendor("Vendor 1")
        sleep(2)
        # ac.clickActive()
        ac.addAdminComment("this is admin comment")
        sleep(1)
        ac.clickSave()
        sleep(3)

        alt_msg = ac.verifyAlert()
        print(alt_msg)
        if "The new customer has been added successfully" in alt_msg:
            self.log_logger.info("customer added successfully")
            assert True

        else:
            self.log_logger.info("add customer failed")
            self.driver.save_screenshot("D:\\SeleniumPython\\Projects\\FITA\\pythonProject1_FITA\\hybrid_framework\\screenshots" + "test_add_save_customer.png")
            assert False

