import pytest
from ...tools.webdriver.webdriver_setup import WebDriverSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        # 创建 WebDriverSetup 实例并启动 WebDriver
        self.webdriver_setup = WebDriverSetup()
        self.driver = self.webdriver_setup.setup()
        yield
        # 在测试结束后关闭 WebDriver
        self.webdriver_setup.teardown()

    def test_login_functionality(self, setup):
        # 打开目标网站
        self.driver.get("https://www.baidu.com/")

        # 设置浏览器窗口大小
        self.driver.set_window_size(1318, 1013)

        # 查找并点击搜索框
        search_box = self.driver.find_element(By.ID, "kw")
        search_box.click()

        # 输入搜索内容
        search_box.send_keys("1111")

        # 查找并点击搜索按钮
        search_button = self.driver.find_element(By.ID, "su")
        search_button.click()

        # 执行鼠标悬停操作
        more_element = self.driver.find_element(By.LINK_TEXT, "更多")
        actions = ActionChains(self.driver)
        actions.move_to_element(more_element).perform()

        # 这里可以添加断言来验证测试结果
        # 例如检查页面标题是否包含预期文本
        assert "1111" in self.driver.title
