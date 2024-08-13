from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebDriverSetup:
    def __init__(self, binary_location=None, driver_path=None):
        self.binary_location = (
            binary_location or r"D:\Develop\DevelopTools\chrome-win64\chrome.exe"
        )
        self.driver_path = (
            driver_path or r"D:\Develop\DevelopTools\chrome-win64\chromedriver.exe"
        )
        self.driver = None

    def setup(self):
        options = Options()
        options.binary_location = self.binary_location
        options.add_experimental_option("detach", True)
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        return self.driver

    def teardown(self):
        if self.driver:
            self.driver.quit()
