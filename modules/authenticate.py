import mysql.connector as MySQLConnctor

import hashlib

class Authenticate:
    def __init__(self, db = MySQLConnctor):
        self.db = db

    def __call__(self, username, password):
        authorized = False
        result = self.db.findone("SELECT id,username,password,status FROM app_chatgpt_user WHERE username = %s", (username,))
        self.db.close
        if result is None:
            return authorized
        if result[3] != 1:
            return authorized
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        enPassword = m.hexdigest()
        if enPassword == result[2]:
            authorized = True
        return authorized