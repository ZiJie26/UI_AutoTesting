import os
import time
from selenium.webdriver.support.wait import WebDriverWait

from tools.cleanup_utils import cleanup_reports
from tools.webdriver_setup import WebDriverSetup


class Base(WebDriverSetup):

    # 如果你需要在 Base 类中增加额外的设置，请使用 setup_method
    def setup_method(self, method):
        super().setup_method(method)
        # 你可以在这里增加 Base 类特有的设置代码，比如元素定位器初始化等
        # 构建报告文件夹的绝对路径
        current_file_path = os.path.abspath(__file__)
        project_root = os.path.dirname(
            os.path.dirname(current_file_path)
        )  # 获取项目根目录
        reports_directory = os.path.join(project_root, "report", "latest")  # 绝对路径

        # 清理超过7天的报告文件
        cleanup_reports(reports_directory, days=7)

    def teardown_method(self, method):
        # 先执行清理任务，然后调用父类的 teardown_method
        super().teardown_method(method)

    # 查找元素方法 封装
    def base_find(self, loc, timeout=30, poll=0.5):
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*loc)
        )

    # 点击元素 方法封装
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入元素 方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本信息 方法封装
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 截图 方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file(
            "../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
        )

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            return True  # 代表元素存在
        except:
            return False  # 代表元素不存在
