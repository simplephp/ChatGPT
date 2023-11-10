import mysql.connector
from mysql.connector import Error

class MySQLConnctor:
    def __init__(self, user, password, host, database) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            return True
        except Error as e:
            print(f"Error: {e}")
            return False
        
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection.cursor.close()
            self.connection = None

    def findone(self, query, params=None):
        if not self.connection and not self.connect():
            return None
        result = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")

        return result

    def query(self, query, params=None):
        if not self.connection and not self.connect():
            return None

        result = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")

        return result

    def execute(self, query, params=None):
        if not self.connection and not self.connect():
            return False

        success = False
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            success = True
        except Error as e:
            print(f"Error: {e}")

        return success
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()