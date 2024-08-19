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

    if len(sys.argv) > 1 and sys.argv[1] in suite_mapping:
        pytest.main([suite_mapping[sys.argv[1]]])
    else:
        pytest.main()


if __name__ == "__main__":
    main()
