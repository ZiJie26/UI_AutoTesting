import time
import pymysql
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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
        options.add_argument("--disable-gpu")  # 在某些情况下，需要禁用GPU加速

        # 启动 ChromeDriver 服务
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.vars = {}

        # 自动登录
        self.login()

        # 从文件加载 Cookie
        # self.load_cookies()

        # 数据库连接
        try:
            self.connection = pymysql.connect(
                host="192.168.10.210",
                port=3306,
                user="root",
                password="root",
                database="test_hospital_admin",
            )
            print("Connected to MySQL database")
        except pymysql.MySQLError as e:
            print(f"Error connecting to MySQL database: {e}")

    def teardown_method(self, method):
        # 保存 Cookie 到文件
        # self.save_cookies()

        # 关闭数据库连接
        if hasattr(self, "connection") and self.connection:
            self.connection.close()
            print("MySQL connection is closed")
        # 关闭浏览器
        self.driver.quit()

    def login(self):
        # 打开登录页面
        self.driver.get("https://prkj-test.aidmed.net/hospital-admin/index")

    def save_cookies(self):
        with open("cookies.json", "w") as file:
            json.dump(self.driver.get_cookies(), file)

    def load_cookies(self):
        try:
            with open("cookies.json", "r") as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
        except FileNotFoundError:
            pass

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
