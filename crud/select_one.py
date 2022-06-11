import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_python"
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

result = cursor.fetchone()

print(result)