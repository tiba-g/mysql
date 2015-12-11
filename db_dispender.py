import mysql.connector
import os

class DbDispenser:

    def __init__(self, host: str, user: str, password: str, db: str, file_path: str):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.file_path = file_path
        self.connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.password, db=self.db)

    def select(self, sentence):
        result_list = []
        try:
            cur = self.connection.cursor()
            cur.execute(sentence)
            data = cur.fetchall()
            for i in data:
                result_list.append(i)
            cur.close()
        finally:
            cur.close()
        return result_list


    def script_executor(self):
        script_list = self._script_reader()
        if not script_list:
            return
        try:
            cur = self.connection.cursor()
            for i in script_list:
                cur.execute(i)
            result = "Succesfully execution!"
        finally:
            cur.close()
            result = "Abortive execution!"
        return result

    def _script_reader(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r') as f:
            result_list = f.readlines()
        return result_list

    def __del__(self):
        self.connection.close()
