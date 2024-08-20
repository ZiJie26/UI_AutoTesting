# 导入你希望包括在测试套件中的测试用例
from cases.testFeature.test_test2 import Test2


# 创建一个测试套件
class Suite:
    def run_tests(self):
        test_cases = [Test2]  # 将测试用例添加到测试套件中

        for test_case in test_cases:
            # 直接调用测试用例
            test_case()
