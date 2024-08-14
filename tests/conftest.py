import logging
import pytest
from datetime import datetime
import os
from logging.handlers import TimedRotatingFileHandler

# 创建日志目录
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 生成带有时间戳的日志文件名
log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d')}.log")

# 配置日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个基于时间的日志轮转处理器
file_handler = TimedRotatingFileHandler(
    log_filename, when="midnight", backupCount=30, encoding="utf-8"
)
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


# 定义命令行选项，允许用户指定日志文件保留的天数
def pytest_addoption(parser):
    parser.addoption(
        "--log-retention",
        action="store",
        default="30",
        help="Number of days to retain log files.",
    )


# 获取命令行选项值
def get_log_retention_days(config):
    return int(config.getoption("--log-retention"))


# 在测试运行结束时执行日志清理
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    retention_days = get_log_retention_days(config)

    # 清理旧日志文件
    now = datetime.now()
    for file in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file)
        try:
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - file_time).days > retention_days:
                os.remove(file_path)
                logger.info(f"Removed old log file: {file}")
        except Exception as e:
            logger.error(f"Error removing log file {file}: {e}")

    # 打印简短的测试摘要信息到日志中
    terminal_summary = terminalreporter.summary_stats
    logger.info("-" * 50 + "Summary" + "-" * 100)  # 添加分割线
    logger.info(f"Summary: {terminal_summary}")
    for line in terminalreporter.stats["failed"]:
        logger.error(f"Failure: {line}")
    logger.info("=" * 50 + "executed once" + "=" * 100)  # 添加分割线


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


@pytest.fixture(autouse=True)
def log_test_details(request):
    logger.info(f"Running test: {request.node.name}")
