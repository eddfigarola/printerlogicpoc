import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils

STR_TITLE_ID = "str_title"


class General:

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element_by_id(self, STR_TITLE_ID)
