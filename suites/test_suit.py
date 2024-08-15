import pytest

# 导入你希望包括在测试套件中的测试用例
from cases.testFeature.test_test1 import TestFirst
from cases.testFeature.test_test2 import TestSec


# 创建一个测试套件
class Suite:
    @pytest.mark.parametrize(
        "test_file",
        ["cases/testFeature/test_test1.py", "cases/testFeature/test_test2.py"],
    )
    def test_suite(self, test_file):
        pytest.main(["-v", test_file])
