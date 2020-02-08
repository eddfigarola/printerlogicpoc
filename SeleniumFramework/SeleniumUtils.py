from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_by_id(self, _id):
    WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, _id)))


def send_data(driver, __element_id, __data):
    wait_for_element_by_id(driver, __element_id)
    elem = driver.find_element_by_id(__element_id)
    elem.send_keys(__data)


def click_element_by_id(driver, _id):
    wait_for_element_by_id(driver, _id)
    elem = driver.find_element_by_id(_id)
    elem.click()


def is_element_with_text(driver, _id, __expected_text):
    wait_for_element_by_id(driver, _id)
    elem = driver.find_element_by_id(_id)
    return elem.is_displayed() & (__expected_text in driver.find_element_by_id("user-menu").get_attribute("text"))