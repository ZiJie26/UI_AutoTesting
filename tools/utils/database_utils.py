import pymysql
import json


class DatabaseUtils:
    def __init__(self, config_file="config/db_config.json"):
        self.config_file = config_file
        self.connection = None
        self.db_config = self._load_db_config()

    def _load_db_config(self):
        # 加载数据库配置文件
        try:
            with open(self.config_file, "r") as file:
                db_config = json.load(file)
            return db_config
        except FileNotFoundError:
            print(f"Configuration file {self.config_file} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.config_file}.")
            return None

    def connect(self):
        # 连接数据库
        if self.connection is None and self.db_config:
            try:
                self.connection = pymysql.connect(
                    host=self.db_config["host"],
                    port=self.db_config["port"],
                    user=self.db_config["user"],
                    password=self.db_config["password"],
                    database=self.db_config["database"],
                )
                print("Connected to MySQL database")
            except pymysql.MySQLError as e:
                print(f"Error connecting to MySQL database: {e}")

    def close(self):
        # 关闭数据库连接
        if self.connection:
            self.connection.close()
            self.connection = None
            print("MySQL connection is closed")

    def get_connection(self):
        # 获取数据库连接
        if self.connection is None:
            raise Exception("Database connection is not established.")
        return self.connection
