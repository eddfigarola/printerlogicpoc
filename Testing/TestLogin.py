import unittest
import SeleniumFramework.Driver
import SeleniumFramework.SeleniumUtils
import Pages.Login
import Pages.Admin
import Config.config

config = Config.config
get_driver = SeleniumFramework.Driver.Driver
selenium_utils = SeleniumFramework.SeleniumUtils
login_page = Pages.Login.Login
admin_page = Pages.Admin.Admin


class SeleniumTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test Execution Started")

    def setUp(self):
        self.driver = get_driver.get_driver()

    def test_login(self):
        user_name = "efigarola"
        self.driver.get(config.default_url)
        login_page.wait_until_page_loads(self.driver)
        login_page.fill_login_form(self.driver)
        admin_page.wait_until_page_loads(self.driver)
        assert (selenium_utils.is_element_with_text(self.driver, "user-menu", user_name))

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
