# tools/utils/database_utils.py
import pymysql
import json


class DatabaseUtils:
    def __init__(self, config_file="config/db_config.json"):
        self.config_file = config_file
        self.connection = None
        self.db_config = self._load_db_config()

    def _load_db_config(self):
        try:
            with open(self.config_file, "r") as file:
                db_config = json.load(file)
            return db_config
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from {self.config_file}.")

    def connect(self):
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
                raise pymysql.MySQLError(f"Error connecting to MySQL database: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("MySQL connection is closed")

    def get_connection(self):
        if self.connection is None:
            raise Exception("Database connection is not established.")
        return self.connection
