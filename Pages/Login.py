import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils


class Login:

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element_by_id(self, "relogin_user")

    def fill_login_form(self, *args):

        if len(args) > 1:
            user = (args[0])
            password = (args[1])
        else:
            user = "efigarola"
            password = "password2020"

        selenium_utils.send_data(self, "relogin_user", user)
        selenium_utils.send_data(self, "relogin_password", password)
        selenium_utils.click_element_by_id(self, "admin-login-btn")
