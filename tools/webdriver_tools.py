from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tools.sl_cookies import CookieManager


class WebDriverTools:
    @staticmethod
    def webdriver_setup(db_utils):
        chrome_testing_path = r"D:\Develop\DevelopTools\chrome-win64\chrome.exe"
        chromedriver_path = r"D:\Develop\DevelopTools\chrome-win64\chromedriver.exe"
        chrome_user_data_dir = (
            r"C:\Users\ChuZijie\AppData\Local\Google\Chrome for Testing\User Data"
        )

        options = webdriver.ChromeOptions()
        options.binary_location = chrome_testing_path
        options.add_experimental_option("detach", True)
        options.add_argument(f"user-data-dir={chrome_user_data_dir}")
        options.add_argument("--profile-directory=Default")

        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        cookie_manager = CookieManager(driver)

        yield {
            "driver": driver,
            "cookie_manager": cookie_manager,
            "db_connection": db_utils.get_connection(),
            "vars": {},
        }

        cookie_manager.save_cookies()
        driver.quit()
