
from os import getenv
#import pymssql
import pyodbc

server      = "(local)"
user        = "sbs\rkrall"
password    = ""
database    = "seis603_pricing_project"

#conn = pymssql.connect(server, user, password, database)
#server=r'RKRALL-7LT64',

conn = pyodbc.connect(
    r'DRIVER={SQL Server Native Client 11.0};'
    r'SERVER=localhost;'
    r'DATABASE=seis603_pricing_project;'
    r'UID=python_dev;'
    r'PWD=python_dev'
    )

cursor = conn.cursor()

cursor.execute('Select * from dbo.Person')

for row in cursor:
    print('row = %r' % (row,))


conn.close()



'''
#calling proc
cursor.callproc('FindPerson', ('Jane Doe',))
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))
'''
