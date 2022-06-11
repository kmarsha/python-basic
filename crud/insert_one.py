import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_python"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Macca", "Bogor")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))