import pymysql
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from tools.webdriver_setup import WebDriverSetup


class TestFirst(WebDriverSetup):
    def test_1(self):
        time.sleep(30)

        # 查询数据库获取最新的 code 数据
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT
                    id, 
                    `code`, 
                    phone_number
                FROM
                    sys_sms_record
                ORDER BY id DESC
                LIMIT 1
                """
                cursor.execute(query)
                result = cursor.fetchone()

                if result:
                    print(
                        f"Latest record - ID: {result[0]}, Code: {result[1]}, Phone Number: {result[2]}"
                    )
                else:
                    print("No records found.")
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")
