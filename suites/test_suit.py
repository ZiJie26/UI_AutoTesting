import pytest


# 创建一个测试套件
class TestSuite:
    def test_test1(self):
        pytest.main(["-v", "cases/testFeature/test_test1.py"])

    def test_test2(self):
        pytest.main(["-v", "cases/testFeature/test_test2.py"])
