from selenium.webdriver.common.by import By
from SeleniumFramework import SeleniumUtils
from Config import config


selenium_utils = SeleniumUtils
config = config


class Login:
    USER_NAME_INPUT_ID = "relogin_user"
    PASSWORD_INPUT_ID = "relogin_password"
    LOGIN_SUBMIT_BUTTON = "admin-login-btn"
    LOGIN_MESSAGE_ID = "logintext"

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element(self, By.ID, Login.USER_NAME_INPUT_ID)

    def fill_login_form(self, *args):

        if len(args) > 1:
            user = (args[0])
            password = (args[1])
        else:
            user = config.default_username
            password = config.default_password

        selenium_utils.send_data(self, Login.USER_NAME_INPUT_ID, user)
        selenium_utils.send_data(self, Login.PASSWORD_INPUT_ID, password)
        selenium_utils.click_element(self, By.ID, Login.LOGIN_SUBMIT_BUTTON)

    def get_login_message(self):
        selenium_utils.get_element_text_by_id(self, Login.LOGIN_MESSAGE_ID)
