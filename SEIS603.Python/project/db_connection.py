from os import getenv
#import pymssql
import pyodbc


def database_connection():
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};'
        r'SERVER=localhost;'
        r'DATABASE=seis603_pricing_project;'
        r'UID=python_dev;'
        r'PWD=python_dev'
        )
    cursor = conn.cursor()
    return cursor
