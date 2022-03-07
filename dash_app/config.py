import os

BASE_PATH = os.getcwd()

DATABASES = {
    'SQL_server': {
        'HOST': "",
        'DATABASE': '',
        'USER': "",
        'PASSWORD': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}
