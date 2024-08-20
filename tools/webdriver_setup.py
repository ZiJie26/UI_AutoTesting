import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tools.sl_cookies import CookieManager
from tools.database_utils import DatabaseUtils


class WebDriverSetup:
    def setup_method(self, method):
        # Chrome 和 ChromeDriver 的路径
        chrome_testing_path = r"D:\Develop\DevelopTools\chrome-win64\chrome.exe"
        chromedriver_path = r"D:\Develop\DevelopTools\chrome-win64\chromedriver.exe"
        chrome_user_data_dir = (
            r"C:\Users\ChuZijie\AppData\Local\Google\Chrome for Testing\User Data"
        )

        # 配置 Chrome 选项
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_testing_path
        options.add_experimental_option("detach", True)
        options.add_argument(f"user-data-dir={chrome_user_data_dir}")
        options.add_argument("--profile-directory=Default")  # 指定个人资料，可区分环境
        # options.add_argument("--headless")  # 启用无头模式
        # options.add_argument("--window-size=1920,1080")  # 根据你的屏幕分辨率调整
        # options.add_argument("--disable-gpu")  # 在某些情况下，需要禁用GPU加速

        # 启动 ChromeDriver 服务
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.cookie_manager = CookieManager(self.driver)
        self.driver.maximize_window()  # 最大化窗口
        self.vars = {}

        # 打开被测主页
        # self.index()

        # 从文件加载 Cookie
        # self.cookie_manager.load_cookies()

        # 初始化数据库连接
        # self.db_utils = DatabaseUtils()
        # self.db_utils.connect()  # 连接数据库

    def teardown_method(self, method):
        # 保存 Cookie 到文件
        self.cookie_manager.save_cookies()

        # 关闭数据库连接
        # self.db_utils.close()

        # 关闭浏览器
        self.driver.quit()

    def index(self):
        # 打开主页
        test_env = "https://prkj-test.aidmed.net/hospital-admin/index"
        self.driver.get(test_env)

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
