import mysql.connector

db= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Secret312040',
    database='test'
)

mycursor = db.cursor()
mycursor.execute("SHOW DATABASES")