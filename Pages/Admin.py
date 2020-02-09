import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils

NODE_TITLE_ID = "node_title"
DELETE_BUTTON_ID = "browse-delete"
PRINTER_ICON_CLASS_NAME = "printer.icon.jstree-icon"
NEW_FOLDER_BUTTON_ID = "newfolder"
ADD_IP_LINK_ID = "addip_link"
PRINTER_NAME_INPUT_ID = "PrinterName"
PRINTER_LOCATION_INPUT_ID = "PrinterLocation_popup"
IP_ADDRESS_INPUT_ID = "IPAddress"
PRINTER_COMMENT_INPUT_ID = "PrinterComment_popup"
ADD_IP_BUTTON_ID = "add_ip_close"

DEFAULT_NEW_PRINTER_NAME = "Test"
DEFAULT_PRINTER_LOCATION = "Test"
DEFAULT_PRINTER_IP_ADDRESS = "Test"
DEFAULT_PRINTER_COMMENT = "Test"

class Admin:

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element_by_id(self, "node_title")

    def delete_printer_by_index(self, index):
        printer_checkbox = self.find_elements_by_class_name(PRINTER_ICON_CLASS_NAME)[index].find_element_by_xpath(
            '..')
        printer_id = printer_checkbox.find_element_by_xpath('..').get_attribute("id")
        printer_checkbox.click()
        printer_checkbox.click()
        selenium_utils.click_element_by_id(self, DELETE_BUTTON_ID)
        selenium_utils.accept_alert(self)
        selenium_utils.wait_for_element_disappears_by_id(self, printer_id)

    def add_new_printer(self, *args):
        if len(args) > 1:
            default_printer_name = (args[0])
            default_printer_location = (args[1])
        else:
            default_printer_name = DEFAULT_NEW_PRINTER_NAME
            default_printer_location = DEFAULT_PRINTER_LOCATION

        default_printer_ip_address = DEFAULT_PRINTER_IP_ADDRESS
        default_printer_comment = DEFAULT_PRINTER_COMMENT

        selenium_utils.wait_for_element_by_id(self, NEW_FOLDER_BUTTON_ID)
        selenium_utils.click_element_by_id(self, NEW_FOLDER_BUTTON_ID)
        selenium_utils.wait_for_element_by_id(self, ADD_IP_LINK_ID)
        selenium_utils.click_element_by_id(self, ADD_IP_LINK_ID)
        selenium_utils.wait_for_element_by_id(self, PRINTER_NAME_INPUT_ID)
        selenium_utils.send_data(self, PRINTER_NAME_INPUT_ID, default_printer_name)
        selenium_utils.send_data(self, PRINTER_LOCATION_INPUT_ID, default_printer_location)
        selenium_utils.send_data(self, IP_ADDRESS_INPUT_ID, default_printer_ip_address)
        selenium_utils.send_data(self, PRINTER_COMMENT_INPUT_ID, default_printer_comment)
        selenium_utils.click_element_by_id(self, ADD_IP_BUTTON_ID)

    def get_count_of_printer(self):
        return selenium_utils.get_count_of_elements_with_class(self, PRINTER_ICON_CLASS_NAME)
