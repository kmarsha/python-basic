print("=====Bangun Datar dan Bangun Ruang=====")
print("1. Bangun Datar\n2. Bangun Ruang")

pilihan = int(input("Masukkan Pilihan:"))

if pilihan == 1:
  print("===Bangun Datar===")
  print("1. Persegi\n2. Persegi Panjang\n3. Jajargenjang")

  pilihan_datar = int(input("Pilih Bangun Datar:"))

  if pilihan_datar == 1:
    sisi = int(input("Masukkan Sisi:"))
    keliling = 4 * sisi
    luas = sisi*sisi
    print("Keliling Persegi: ", keliling, "\nLuas Persegi: ", luas)
  elif pilihan_datar == 2:
    p = int(input("Masukkan Panjang:"))
    l = int(input("Masukkan Lebar:"))
    keliling = 2*(p+l)
    luas = p*l
    print("Keliling Persegi Panjang: ", keliling, "\nLuas Persegi Panjang:", luas)
  elif pilihan_datar == 3:
    a = int(input("Masukkan Sisi A:"))
    b = int(input("Masukkan Sisi B:"))
    c = int(input("Masukkan Sisi C:"))
    d = int(input("Masukkan Sisi D:"))
    t = int(input("Masukkan Tinggi:"))
    keliling = a + b + c + d
    luas = a * t
    print("Keliling Jajargenjang:", keliling, "\nLuas Jajargenjang:", luas)
  else:
    print("Pilihan Bangun Datar Tidak Ada")
elif pilihan == 2:
  print("===Bangun Ruang===")
  print("1. Kubus\n2. Balok\n3. Bola")

  pilihan_ruang = int(input("Pilih Bangun Ruang: "))

  if pilihan_ruang == 1:
    rusuk = int(input("Masukkan Rusuk:"))
    luas = 6 * (rusuk**2)
    volume = rusuk**3
    print("Luas Kubus: ", luas, "\nVolume Kubus: ", volume)
  elif pilihan_ruang == 2:
    p = int(input("Masukkan Panjang:"))
    l = int(input("Masukkan Lebar:"))
    t = int(input("Masukkan Tinggi:"))
    luas = (2*p*l) + (2*p*t) + (2*l*t)
    volume = p*l*t
    print("Luas Balok: ", luas, "\nVolume Balok:", volume)
  elif pilihan_ruang == 3:
    r = int(input("Masukkan Jari-jari:"))
    phi = 3.14
    luas = 4 * phi * (r**2)
    volume = (4/3) * phi * (r**3)
    print("Luas Bola: ", luas, "\nVolume Bola: ", volume)
  else:
    print("Pilihan Bangun Ruang Tidak Ada")
else:
  print("Pilihan Tidak Ada.")