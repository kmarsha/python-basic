import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_python"
)

cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("Macca", "Bogor", 1)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))