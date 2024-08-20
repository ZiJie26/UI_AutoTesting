import logging
import pytest
import datetime
from datetime import datetime
import os
from logging.handlers import TimedRotatingFileHandler

from tools.cleanup_utils import cleanup_reports
from tools.database_utils import DatabaseUtils
from tools.webdriver_tools import WebDriverTools

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


def get_log_retention_days(config):
    # 示例：从 config 中获取日志保留天数
    return config.getoption("--log-retention-days", default=30)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    log_dir = "logs"  # 请替换为你的日志目录路径
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
    logger.info("-" * 50 + " Summary " + "-" * 50)  # 添加分割线
    logger.info(f"Summary: {terminalreporter.summary_stats}")

    # 处理 'failed' 键
    failed_tests = terminalreporter.stats.get("failed", [])
    for line in failed_tests:
        logger.error(f"Failure: {line}")

    logger.info("=" * 50 + " Executed Once " + "=" * 50)  # 添加分割线


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


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 获取当前日期
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # 设置报告文件名
    report_path = f"report/latest/report_{date_str}.html"
    # 更新 pytest 的 addopts
    config.option.htmlpath = report_path


@pytest.fixture(scope="session")
def db_utils():
    db_utils_instance = DatabaseUtils()
    db_utils_instance.connect()
    yield db_utils_instance
    db_utils_instance.close()


@pytest.fixture(scope="function", name="ws")
def webdriver_setup(db_utils):
    ws_gen = WebDriverTools.webdriver_setup(db_utils)
    ws = next(ws_gen)  # 获取生成器返回的字典
    yield ws  # 将字典传递给测试用例
    try:
        next(ws_gen)  # 执行清理逻辑
    except StopIteration:
        pass


@pytest.fixture(autouse=True)
def cleanup_reports_fixture():
    reports_directory = "report/latest"
    cleanup_reports(reports_directory, days=7)
