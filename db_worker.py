import sqlite3
import os



class DBWorker:
    def __init__(self):
        self.db_name = os.getenv('DB_NAME')


    def get_connection(self):
        ...


