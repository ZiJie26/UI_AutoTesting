import os
import pytest
import sys

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

# 添加项目根目录到sys.path
sys.path.append(project_root)


def main():
    suite_mapping = {
        "test1": "suites/suit1.py",
        "test2": "suites/suit2.py",
        # 添加更多的映射
    }

    # 收集所有有效的测试套件路径
    test_suites = []
    for arg in sys.argv[1:]:
        if arg in suite_mapping:
            test_suites.append(suite_mapping[arg])

    if test_suites:
        pytest.main(test_suites)
    else:
        pytest.main()


if __name__ == "__main__":
    main()
