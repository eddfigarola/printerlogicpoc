import SeleniumFramework.Driver
import unittest
import Pages.Login
import Pages.Admin
import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils
get_driver = SeleniumFramework.Driver.Driver
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
        password = "password2020"
        self.driver.get("https://trial2020.printercloud.com/admin/")
        login_page.wait_until_page_loads(self.driver)
        login_page.fill_login_form(self.driver, user_name, password)
        admin_page.wait_until_page_loads(self.driver)
        assert (selenium_utils.is_element_with_text(self.driver, "user-menu", user_name))

    def test_login_two(self):
        user_name = "efigarola"
        password = "invalid"
        self.driver.get("https://trial2020.printercloud.com/admin/")
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
