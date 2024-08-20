import time

import pytest
from selenium.webdriver.common.by import By


class Test2:
    @pytest.mark.demo
    def test_2(self, ws):
        # Test name: 2
        # Step # | name | target | value
        # 1 | open | / |
        ws.driver.get("https://www.baidu.com/")
        # 2 | setWindowSize | 1318x1013 |
        ws.driver.set_window_size(1318, 1013)
        # 3 | click | css=.hotsearch-item:nth-child(1) .title-content-title |
        ws.vars["window_handles"] = ws.driver.window_handles
        # 4 | selectWindow | handle=${win4315} |
        ws.driver.find_element(
            By.CSS_SELECTOR, ".hotsearch-item:nth-child(1) .title-content-title"
        ).click()
        ws.vars["win4315"] = ws.wait_for_window(2000)
        ws.driver.switch_to.window(self.vars["win4315"])  # type: ignore
