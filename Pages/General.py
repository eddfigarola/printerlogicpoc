import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils


class General:

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element_by_id(self, "str_title")

