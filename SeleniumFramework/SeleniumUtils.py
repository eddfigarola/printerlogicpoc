from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_WAIT_TIME = 30


def accept_alert(self):
    alert_obj = self.switch_to.alert
    alert_obj.accept()


def wait_for_element_by_id(self, _id):
    WebDriverWait(self, DEFAULT_WAIT_TIME).until(EC.presence_of_element_located((By.ID, _id)))


def wait_for_element(self, __selector, _selector_value):
    WebDriverWait(self, DEFAULT_WAIT_TIME).until(EC.presence_of_element_located((__selector, _selector_value)))


def wait_for_element_disappears(self, __selector, __selector_value):
    WebDriverWait(self, DEFAULT_WAIT_TIME).until(EC.invisibility_of_element((__selector, __selector_value)))


def send_data(driver, __selector, __selector_value, __data):
    wait_for_element(driver, __selector, __selector_value)
    elem = driver.find_element(__selector, __selector_value)
    elem.send_keys(__data)


def get_element_text_by_id(driver, __element_id):
    wait_for_element_by_id(driver, __element_id)
    return driver.find_element_by_id(__element_id).get_attribute("text")


def drag_element_by_id(driver, _id, __x, __y):
    wait_for_element_by_id(driver, _id)


def click_element(driver, __selector, __selector_value):
    wait_for_element(driver, __selector, __selector_value)
    elem = driver.find_element(__selector, __selector_value)
    elem.click()


def click_element_by_id(driver, _id):
    wait_for_element_by_id(driver, _id)
    elem = driver.find_element_by_id(_id)
    elem.click()


def is_element_with_text(driver, _id, __expected_text):
    wait_for_element_by_id(driver, _id)
    elem = driver.find_element_by_id(_id)
    return elem.is_displayed() & (__expected_text in driver.find_element_by_id("user-menu").get_attribute("text"))


def get_count_of_elements_with_class(driver, __class_name):
    elements = driver.find_elements_by_class_name(__class_name)
    return len(elements)
