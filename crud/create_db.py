import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE db_python")

print("Database berhasil dibuat!")