import unittest
import SeleniumFramework.Driver
import SeleniumFramework.SeleniumUtils
import Pages.Login
import Pages.Admin
import Pages.General

get_driver = SeleniumFramework.Driver.Driver
selenium_utils = SeleniumFramework.SeleniumUtils
login_page = Pages.Login.Login
admin_page = Pages.Admin.Admin
general_tab = Pages.General.General


class SeleniumTestsAdmin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test Execution Started")

    def setUp(self):
        self.driver = get_driver.get_driver()
        self.driver.get("https://trial2020.printercloud.com/admin/")
        login_page.wait_until_page_loads(self.driver)
        login_page.fill_login_form(self.driver)
        admin_page.wait_until_page_loads(self.driver)

    def test_add_printer(self):
        initial_printers_count = admin_page.get_count_of_printer(self.driver)
        admin_page.add_new_printer(self.driver)
        general_tab.wait_until_page_loads(self.driver)
        final_printers_count = admin_page.get_count_of_printer(self.driver)

        assert (final_printers_count == initial_printers_count + 1)

    def test_delete_printer(self):
        initial_printers_count = admin_page.get_count_of_printer(self.driver)
        admin_page.delete_printer_by_index(self.driver, 0)
        final_printers_count = admin_page.get_count_of_printer(self.driver)
        assert (final_printers_count == (initial_printers_count - 1))

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        print("Test Execution Completed")


if __name__ == '__main__':
    unittest.main()
