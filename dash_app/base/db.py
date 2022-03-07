from abc import ABC, abstractmethod
from dash_app import config


class DbInstance(ABC):
    """
    interface to create db instancs and
    defining set of functions
    """
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_connection_string(self):
        pass

    @abstractmethod
    def execute_many(self):
        pass


class MssqlInstance(DbInstance):
    """
    MSSQL db instance which is based on the above abstract class
    provides db adaptor functionality
    """
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        """
        returns the conn
        """
        import pyodbc

        # parameter dictionary
        param_dic = {
            'driver': config.DATABASES['SQL_server']['OPTIONS']['driver'],
            'server': self.host,
            'database': self.database,
            'uid': self.user,
            'pwd': self.password
        }

        conn = None
        try:
            conn = pyodbc.connect(*param_dic)
        except Exception as error:
            print(error)

    def get_connection_string(self):
        return f"host is: {self.host}, user is {self.user}, and database is {self.database}"

    def execute_many(self, cursor, query, chunk, fast_execute=True):
        """
        Try to use fast execute many for sql server if flag in Dbparams is set
        cursor: database cursor
        query: sql query
        chunk: list, rows of parameters
        """
        try:
            cursor.fast_executemany = fast_execute
            cursor.executemany(query, chunk)
            cursor.commit()
        except MemoryError:
            cursor.fast_executemany = False
            cursor.executemany(query, chunk)
            cursor.commit()

    def __str__(self):
        return self.get_connection_string()

    def __repr(self):
        return self.get_connection_string()
