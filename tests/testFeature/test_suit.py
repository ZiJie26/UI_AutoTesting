import pytest

# 导入你希望包括在测试套件中的测试用例
from base_test import TestLogin


# 创建一个测试套件
@pytest.mark.usefixtures("setup")
class AuthSuite:
    @pytest.mark.parametrize("test_case", [TestLogin])
    def test_cases(self, test_case):
        # 运行指定的测试用例
        test_instance = test_case()
        test_instance.test_login_functionality()
