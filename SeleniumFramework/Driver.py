from selenium import webdriver


class Driver:


    @staticmethod
    def get_driver():
        return webdriver.Firefox()

    @staticmethod
    def close_driver(driver):
        driver.quit()
