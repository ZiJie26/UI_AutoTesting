import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebDriverSetup:
    def setup_method(self, method):
        chrome_testing_path = r"D:\Develop\DevelopTools\chrome-win64\chrome.exe"
        chromedriver_path = r"D:\Develop\DevelopTools\chrome-win64\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_testing_path
        options.add_experimental_option("detach", True)
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
