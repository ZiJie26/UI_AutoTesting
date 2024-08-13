import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from tools.webdriver.webdriver_setup import WebDriverSetup


class TestFirst(WebDriverSetup):
    def test_1(self):
        # Test name: 1
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://www.baidu.com/")
        # 2 | setWindowSize | 1318x1013 |
        self.driver.set_window_size(1318, 1013)
        # 3 | click | id=kw |
        self.driver.find_element(By.ID, "kw").click()
        # 4 | type | id=kw | 1111
        self.driver.find_element(By.ID, "kw").send_keys("1111")
        # 5 | click | id=su |
        self.driver.find_element(By.ID, "su").click()
        # 6 | mouseOver | linkText=更多 |
        element = self.driver.find_element(By.LINK_TEXT, "更多")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(5)
        current_url = self.driver.current_url
        assert "qq.com" in current_url, f"当前 URL 不正确: {current_url}"
        print("测试通过: 当前网站为 baidu.com")
