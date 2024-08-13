import pytest
import sys


def main():
    suite_mapping = {
        "test": "tests/testFeature/test_suit.py",
        # 添加更多的映射
    }

    if len(sys.argv) > 1 and sys.argv[1] in suite_mapping:
        pytest.main([suite_mapping[sys.argv[1]]])
    else:
        pytest.main()


if __name__ == "__main__":
    main()
