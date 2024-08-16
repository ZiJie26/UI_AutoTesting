import time

import pytest
from selenium.webdriver.common.by import By

from tools.webdriver_setup import WebDriverSetup


class TestSec(WebDriverSetup):
    def test_2(self):
        # Test name: 2
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://www.baidu.com/")
        # 2 | setWindowSize | 1318x1013 |
        self.driver.set_window_size(1318, 1013)
        # 3 | click | css=.hotsearch-item:nth-child(1) .title-content-title |
        self.vars["window_handles"] = self.driver.window_handles
        # 4 | selectWindow | handle=${win4315} |
        self.driver.find_element(
            By.CSS_SELECTOR, ".hotsearch-item:nth-child(1) .title-content-title"
        ).click()
        self.vars["win4315"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win4315"])  # type: ignore
