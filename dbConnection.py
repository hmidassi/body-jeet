import sqlite3

class dbConnection(object):


    def __init__(self,dbName):
        self.dbName=dbName

    def createConnection(self):
        connection=sqlite3.connect(self.dbName)
        return connection

    def createCursor(self,connection):
        cursor=connection.cursor()
        return cursor

connectionManager=dbConnection("dbAppliBodyJeet")
conn=connectionManager.createConnection()
cursor=connectionManager.createCursor(conn)
cursor.execute("SELECT * FROM CATEGORIE_EXERCICE")

for line in cursor:
    print(line)
