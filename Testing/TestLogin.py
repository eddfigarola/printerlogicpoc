import unittest
from SeleniumFramework import Driver, SeleniumUtils
from Pages import Login, Admin
from Config import config

config = config
get_driver = Driver.Driver
selenium_utils = SeleniumUtils
login_page = Login.Login
admin_page = Admin.Admin


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test Execution Started")

    def setUp(self):
        self.driver = get_driver.get_driver()

    def test_login(self):
        self.driver.get(config.default_url)
        login_page.wait_until_page_loads(self.driver)
        login_page.fill_login_form(self.driver)
        admin_page.wait_until_page_loads(self.driver)
        assert (selenium_utils.is_element_with_text(self.driver, "user-menu", config.default_username))

    def test_login_empty_form(self):
        user_name = ""
        password = ""
        self.driver.get(config.default_url)
        login_page.wait_until_page_loads(self.driver)
        login_page.fill_login_form(self.driver, user_name, password)

        try:
            admin_page.wait_until_page_loads(self.driver)
        except:
            pass
        else:
            self.fail("Access was allowed with empty form")

    def test_login_invalid_password(self):
        user_name = "efigarola"
        password = "invalid"
        self.driver.get(config.default_url)
        login_page.wait_until_page_loads(self.driver)
        login_page.fill_login_form(self.driver, user_name, password)

        try:
            admin_page.wait_until_page_loads(self.driver)
        except:
            pass
        else:
            self.fail("Access was allowed with incorrect password")

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        print("Test Execution Completed")


if __name__ == '__main__':
    unittest.main()
