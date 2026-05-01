from multiprocessing import connection

import pymysql


class Db():
    def __init__(self):
        self._connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "JovanSQL1",
            database = "oop_3"
        )

    def _get_connection(self): # protected method
        return self._connection

