from selenium.webdriver.common.by import By
from SeleniumFramework import SeleniumUtils

selenium_utils = SeleniumUtils


class General:
    STR_TITLE_ID = "str_title"

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element(self, By.ID, General.STR_TITLE_ID)
