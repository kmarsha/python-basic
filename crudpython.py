import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="db_python"
) 

mycursor = db.cursor()

def tampil_data(db):
  mycursor.execute("SELECT * FROM users")
  myresult = mycursor.fetchall()
  print("=======================\n(id, nama, email, no hp)")
  for val in myresult:
    print(val)

def tambah_data(db):
  user_id = input("USER ID:")
  nama = input("NAMA:")
  email = input("EMAIL:")
  no_hp = input("NO HP:")
  sql = "INSERT INTO users (id, nama, email, no_hp) VALUES (%s, %s, %s, %s)"
  val = (user_id, nama, email, no_hp)
  mycursor.execute(sql, val)
  db.commit()
  print(mycursor.rowcount, "Data user berhasil ditambahkan!")

def ubah_data(db):
  id = input("ID USER:")
  mycursor.execute("SELECT * FROM users where id = '" + id + "' LIMIT 1")
  myresult = mycursor.fetchall()
  user = None
  for val in myresult:
    user = val
  
  if (user != None):
    nama = input("Nama ("+user[1]+") :") or user[1]
    email = input("Email ("+user[2]+") :") or user[2]
    no_hp = input("No HP ("+user[3]+") :") or user[3]
    sql = "UPDATE users SET nama=%s, email=%s, no_hp=%s WHERE id=%s"
    val = (nama, email, no_hp, id)
    mycursor.execute(sql, val)
    db.commit()
    print(mycursor.rowcount, "Data user berhasil diubah!")
  else:
    print("Data tidak ditemukan!")

def hapus_data(db):
  id = input("ID USER: ")
  mycursor.execute("SELECT * FROM users WHERE id='"+id+"' LIMIT 1")
  myresult = mycursor.fetchall()
  user = None
  for val in myresult:
    user = val
  if (user != None):
    print("MENGHAPUS DATA: ", user)
    sql = "DELETE FROM users WHERE id = " + id
    mycursor.execute(sql)
    db.commit()
    print(mycursor.rowcount, "Data user berhasil dihapus!")
  else:
    print("Data tidak ditemukan!")

lanjut = True
while lanjut:
  print("\n\n\nCRUD User\n1.LIHAT USER\n2.TAMBAH USER\n3.UBAH USER\n4.HAPUS USER\n5.KELUAR\n")

  pilih = int(input("PILIH MENU:"))
  print("\n\n\n")
  if(pilih == 1):
    tampil_data(db)
  elif(pilih == 2):
    tambah_data(db)
  elif(pilih == 3):
    ubah_data(db)
  elif(pilih == 4):
    hapus_data(db)
  elif(pilih == 5):
    keluar = input("Apakah Anda yakin akan keluar?")
    if (keluar == 'y' or keluar == 'ya'):
      print("bye, bye!")
      lanjut = False
  else:
    print("Pilihan tidak tersedia!")