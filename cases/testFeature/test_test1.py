import pymysql
import pytest


class Test1:
    @pytest.mark.demo
    def test_1(self, ws):
        driver = ws["driver"]
        driver.get("https://www.baidu.com")
        # 获取数据库连接
        connection = ws["db_connection"]

        # 执行查询
        try:
            with connection.cursor() as cursor:
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
