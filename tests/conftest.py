import logging
import pytest
from datetime import datetime
import os

# 创建日志目录
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 生成带有时间戳的日志文件名
log_filename = os.path.join(
    log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# 配置日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个文件处理器
file_handler = logging.FileHandler(log_filename, "a", encoding="utf-8")
file_handler.setLevel(logging.INFO)

# 创建一个控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建一个日志格式器并设置给处理器
formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def pytest_runtest_logreport(report):
    if report.when == "call":  # 只在测试用例执行完成时记录
        if report.passed:
            logger.info(f"Test {report.nodeid} PASSED")
        elif report.failed:
            # 打印失败原因
            logger.error(f"Test {report.nodeid} FAILED")
            logger.error(f"Failure reason: {report.longrepr}")
        elif report.skipped:
            logger.warning(f"Test {report.nodeid} SKIPPED")


@pytest.hookimpl(tryfirst=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """在测试运行结束后打印简短的测试摘要信息到日志中"""
    terminal_summary = terminalreporter.summary_stats
    logger.info("=" * 100)  # 添加分割线
    logger.info(f"Summary: {terminal_summary}")
    for line in terminalreporter.stats["failed"]:
        logger.error(f"Failure: {line}")


@pytest.fixture(autouse=True)
def log_test_details(request):
    logger.info(f"Running test: {request.node.name}")
