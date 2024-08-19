import json
import os


class CookieManager:
    def __init__(self, driver, file_name="cookies.json"):
        self.driver = driver
        # 设置文件路径为项目根目录下的 config 目录
        self.file_path = os.path.join("config", file_name)

    def save_cookies(self):
        """Save cookies to a JSON file."""
        os.makedirs(
            os.path.dirname(self.file_path), exist_ok=True
        )  # 确保 config 目录存在
        with open(self.file_path, "w") as file:
            json.dump(self.driver.get_cookies(), file)

    def load_cookies(self):
        """Load cookies from a JSON file and add them to the browser."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
