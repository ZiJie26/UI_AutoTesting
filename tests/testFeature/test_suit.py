import pytest

# 导入你希望包括在测试套件中的测试用例
from tests.testFeature.test_test1 import TestFirst
from tests.testFeature.test_test2 import TestSec


# 创建一个测试套件
@pytest.mark.usefixtures("setup")
class AuthSuite:
    def test_1(self):
        test_instance = TestFirst()
        pytest.main(["-v", "tests/testFeature/test_test1.py"])

    def test_2(self):
        test_instance = TestSec()
        pytest.main(["-v", "tests/testFeature/test_test2.py"])
