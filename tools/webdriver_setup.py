# tools/webdriver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tools.utils.sl_cookies import CookieManager
from tools.utils.database_utils import DatabaseUtils


class WebDriverSetup:
    def __init__(self):
        # Chrome 和 ChromeDriver 的路径
        self.chrome_testing_path = r"D:\Develop\DevelopTools\chrome-win64\chrome.exe"
        self.chromedriver_path = (
            r"D:\Develop\DevelopTools\chrome-win64\chromedriver.exe"
        )
        self.chrome_user_data_dir = (
            r"C:\Users\ChuZijie\AppData\Local\Google\Chrome for Testing\User Data"
        )

        # 配置 Chrome 选项
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.chrome_testing_path
        self.options.add_experimental_option("detach", True)
        self.options.add_argument(f"user-data-dir={self.chrome_user_data_dir}")
        self.options.add_argument("--profile-directory=Default")

        self.service = Service(self.chromedriver_path)

        self.driver = None
        self.cookie_manager = None
        self.db_utils = None
        self.vars = {}

    def setup(self):
        # 启动 ChromeDriver 服务
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.cookie_manager = CookieManager(self.driver)
        self.driver.maximize_window()
        self.db_utils = DatabaseUtils()
        self.db_utils.connect()

    def teardown(self):
        if self.cookie_manager:
            self.cookie_manager.save_cookies()
        if self.db_utils:
            self.db_utils.close()
        if self.driver:
            self.driver.quit()
