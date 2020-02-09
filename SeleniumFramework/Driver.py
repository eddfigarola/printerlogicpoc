from selenium import webdriver


class Driver:


    @staticmethod
    def get_driver():
        return webdriver.Firefox(service_log_path='../Logs/geckodriver.log')

    @staticmethod
    def close_driver(driver):
        driver.quit()
