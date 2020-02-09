from selenium import webdriver

from selenium.webdriver.firefox.options import Options
import Config.config

config = Config.config


class Driver:

    @staticmethod
    def get_driver():
        options = Options()
        options.headless = config.headless
        return webdriver.Firefox(options=options, service_log_path='../Logs/geckodriver.log')

    @staticmethod
    def close_driver(driver):
        driver.quit()
