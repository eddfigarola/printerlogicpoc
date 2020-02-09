import SeleniumFramework.SeleniumUtils

selenium_utils = SeleniumFramework.SeleniumUtils


class Admin:

    def wait_until_page_loads(self):
        selenium_utils.wait_for_element_by_id(self, "node_title")

    def delete_printer_by_index(self, index):
        delete_button = "browse-delete"
        printer_checkbox = self.find_elements_by_class_name("printer.icon.jstree-icon")[index].find_element_by_xpath('..')
        printer_id = printer_checkbox.find_element_by_xpath('..').get_attribute("id")
        printer_checkbox.click()
        printer_checkbox.click()
        selenium_utils.click_element_by_id(self, delete_button)
        alert_obj = self.switch_to.alert
        alert_obj.accept()
        selenium_utils.wait_for_element_disappears_by_id(self, printer_id)


    def add_new_printer(self):
        new_folder_button = "newfolder"
        add_ip_link = "addip_link"
        printer_name_input = "PrinterName"
        printer_location_input = "PrinterLocation_popup"
        ip_address_input = "IPAddress"
        printer_comment_input = "PrinterComment_popup"
        add_ip_button = "add_ip_close"
        selenium_utils.wait_for_element_by_id(self, new_folder_button)
        selenium_utils.click_element_by_id(self,new_folder_button)
        selenium_utils.wait_for_element_by_id(self, add_ip_link)
        selenium_utils.click_element_by_id(self, add_ip_link)
        selenium_utils.wait_for_element_by_id(self, printer_name_input)
        selenium_utils.send_data(self, printer_name_input, "test")
        selenium_utils.send_data(self, printer_location_input, "test")
        selenium_utils.send_data(self, ip_address_input, "test")
        selenium_utils.send_data(self, printer_comment_input, "test")
        selenium_utils.click_element_by_id(self, add_ip_button)

    def get_count_of_printer(self):
        printer_icon_class = "printer.icon.jstree-icon"
        return selenium_utils.get_count_of_elements_with_class(self, printer_icon_class)