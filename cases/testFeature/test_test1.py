import pymysql
import pytest

from page.base_page import Base


class Test1(Base):
    @pytest.mark.demo
    def test_1(self):
        self.driver.get("https://www.qq.com/")

    # def test_1(self, db_connection):
    #     """
    #     这个方法为数据库查询的模板代码
    #     需要在config\db_config.json里填上正确的数据库信息才能用哦~
    #     """
    #     # 获取数据库连接
    #     connection = db_connection

    #     # 执行查询
    #     try:
    #         with connection.cursor() as cursor:
    #             query = """
    #             SELECT
    #                 id,
    #                 `code`,
    #                 phone_number
    #             FROM
    #                 sys_sms_record
    #             ORDER BY id DESC
    #             LIMIT 1
    #             """
    #             cursor.execute(query)
    #             result = cursor.fetchone()

    #             if result:
    #                 print(
    #                     f"Latest record - ID: {result[0]}, Code: {result[1]}, Phone Number: {result[2]}"
    #                 )
    #             else:
    #                 print("No records found.")
    #     except pymysql.MySQLError as e:
    #         print(f"Error executing query: {e}")
