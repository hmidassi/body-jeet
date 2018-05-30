import sqlite3

def createConnection():
    connection=sqlite3.connect("dbAppliBodyJeet")
    return connection

def createCursor(connection):
    cursor=connection.cursor()
    return cursor

conn=createConnection()
cursor=createCursor(conn)
cursor.execute("SELECT * FROM CATEGORIE_EXERCICE")

for line in cursor:
    print(line)
