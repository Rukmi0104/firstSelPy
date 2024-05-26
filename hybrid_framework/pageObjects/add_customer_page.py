import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ss_folder = r"D:\\SeleniumPython\\Projects\\FITA\\pythonProject1_FITA\\hybrid_framework\\screenshots\\"


class add_customer_page:
    cust_menu_drp_xpath = "//ul[@role='menu']/li/a/p[contains(text(), 'Customers')]"
    cust_submenu_drp_xpath = "//ul[@role='menu']/li/ul/li/a/p[contains(text(), ' Customers')]"
    add_new_button_xpath = "//form/div[@class='content-header clearfix']/div/a"
    email_txt_xpath = "//input[@id='Email']"
    pass_txt_xpath = "//input[@id='Password']"
    f_name_txt_xpath = "//input[@id='FirstName']"
    l_name_txt_xpath = "//input[@id='LastName']"
    male_radio_id = "Gender_Male"
    female_radio_id = "Gender_Female"
    DOB_date_picker_id = "DateOfBirth"
    company_name_txt_xpath = "//input[@id='Company']"
    ts_tax_exempt_checkbox_xpath = "//input[@id='IsTaxExempt']"
    newsletter_combobox_txt_id = "SelectedNewsletterSubscriptionStoreIds"
    newLetter_input_id = "SelectedNewsletterSubscriptionStoreIds"
    your_store_name_drp_id = "select2-SelectedNewsletterSubscriptionStoreIds-result-9728-1"
    test_store_2_drp_id = "select2-SelectedNewsletterSubscriptionStoreIds-result-oarb-2"
    clear_custoRole_txt_xpath = "//span[@class = 'select2-selection__choice__remove']"
    customer_role_combobox_txt_id = "SelectedCustomerRoleIds"
    cust_role_vendors_drp_id = "select2-SelectedCustomerRoleIds-result-wnk2-5"
    cust_role_guests_drp_id = "select2-SelectedCustomerRoleIds-result-scnf-4"
    cust_role_registered_drp_id = "select2-SelectedCustomerRoleIds-result-f121-3"
    cust_role_forum_moderator_drp_id = "select2-SelectedCustomerRoleIds-result-58jj-2"
    cust_role_admin_drp_id = "select2-SelectedCustomerRoleIds-result-uswm-1"
    manager_of_vendor_drp_id = "VendorId"
    active_checkbox_id = "Active"
    admin_comment_txt_id = "AdminComment"
    save_button_xpath = "//button[@name='save']"
    success_alert_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def navigateCustomerPage(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.cust_menu_drp_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, self.cust_submenu_drp_xpath).click()

    def clickAddNewButton(self):
        self.driver.find_element(By.XPATH, self.add_new_button_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_txt_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.pass_txt_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.f_name_txt_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.l_name_txt_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.ID, self.male_radio_id).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.ID, self.female_radio_id).click()
        else:
            raise Exception(f"input gender option {gender} is not available")

    def setDOB(self, day, month, yr):
        self.driver.find_element(By.ID, self.DOB_date_picker_id).send_keys(date)

    def setCompanyName(self, cname):
        self.driver.find_element(By.XPATH, self.company_name_txt_xpath).send_keys(cname)

    def clickTaxExempt(self):
        tax_ele = self.driver.find_element(By.XPATH, self.ts_tax_exempt_checkbox_xpath)
        if not tax_ele.is_selected():
            self.driver.find_element(By.XPATH, self.ts_tax_exempt_checkbox_xpath).click()

    def setNewsLetter(self, drpValue):
        # self.driver.find_element(By.ID, self.newLetter_input_id).click()
        # sleep(2)
        sel_newsletter_drop= Select(self.driver.find_element(By.ID, self.newLetter_input_id))
        sel_newsletter_drop.select_by_visible_text(drpValue)

    def setCustomerRole(self, role):
        # self.driver.find_element(By.XPATH, self.clear_custoRole_txt_xpath).click()
        cust_drop_sel = Select(self.driver.find_element(By.ID, self.customer_role_combobox_txt_id))
        if role != "Registered":
            cust_drop_sel.select_by_visible_text(role)
        elif role != "Guests":
            pass

    def select_vendor(self, vendor):
        sel_vendor_drp = Select(self.driver.find_element(By.ID, self.manager_of_vendor_drp_id))
        if vendor == "Vendor 1":
            sel_vendor_drp.select_by_visible_text("Vendor 1")
        elif vendor == "Vendor 2":
            sel_vendor_drp.select_by_visible_text("Vendor 2")
        elif vendor == "Not a vendor":
            sel_vendor_drp.select_by_visible_text("Not a vendor")
        else:
            raise Exception(f"'invalid input': '{vendor}' is not present in the Manager of vendor list")

    def clickActive(self):
        active_ele = self.driver.find_element(By.ID, self.active_checkbox_id)
        if not active_ele.is_selected():
            active_ele.click()
        else:
            pass

    def addAdminComment(self, textMsg):
        self.driver.find_element(By.ID, self.admin_comment_txt_id).send_keys(textMsg)

    def clickSave(self):
        # actionC = ActionChains(self.driver)
        # actionC.scroll_by_amount(0, -3000).perform()
        # sleep(3)
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        self.driver.save_screenshot(ss_folder + "clickSave.png")

    def verifyAlert(self):
        alert_success_text = self.driver.find_element(By.XPATH, self.success_alert_xpath).text
        return alert_success_text
