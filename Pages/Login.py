from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils


class Login:

    def __init__(self, driver):
        self.driver = driver.get_driver()
        self.USER_INPUT_ID = "relogin_user"

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element_by_id(self, "relogin_user")

    def fill_login_form(self):
        selenium_utils.send_data(self , "relogin_user", "efigarola")
        selenium_utils.send_data(self, "relogin_password", "C1apec0d")
        selenium_utils.click_element_by_id(self, "admin-login-btn")

    def fill_login_form(self, username, password):
        selenium_utils.send_data(self , "relogin_user", username)
        selenium_utils.send_data(self, "relogin_password", password)
        selenium_utils.click_element_by_id(self, "admin-login-btn")
