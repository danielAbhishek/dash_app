import pandas as pd

from dash_app.base.db import MssqlInstance
from dash_app.config import DATABASES

# creating SQL server db instance
MSSQL = MssqlInstance(DATABASES['SQL_server']['HOST'],
                      DATABASES['SQL_server']['DATABASE'],
                      DATABASES['SQL_server']['USER'],
                      DATABASES['SQL_server']['PASSWORD'])


class Model():
    """
    Model class that is responsible to handle data tables
    """
    def __init__(self):
        self.db = MSSQL
        self.df = None
        self.conn = None
        self.cursor = None

    def change_database(self, db):
        self.db.database = db

    def connect(self):
        self.conn = self.db.connect()
        return self.conn

    def get_cursor(self):
        self.cursor = self.connect().cursor()
        return self.cursor

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def get_dataframe(self, dictionary):
        self.df = pd.DataFrame(dictionary)
        return self.df

    def csv_to_dataframe(self, csv):
        self.df = pd.read_csv(csv)
        return self.df
