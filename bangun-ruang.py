print("===Bangun Ruang===")
print("1. Kubus\n2. Balok\n3. Bola")

pilihan = int(input("Pilih Bangun Ruang: "))

if pilihan == 1:
  rusuk = int(input("Masukkan Rusuk:"))
  luas = 6 * (rusuk**2)
  volume = rusuk**3
  print("Luas Kubus: ", luas, "\nVolume Kubus: ", volume)
elif pilihan == 2:
  p = int(input("Masukkan Panjang:"))
  l = int(input("Masukkan Lebar:"))
  t = int(input("Masukkan Tinggi:"))
  luas = (2*p*l) + (2*p*t) + (2*l*t)
  volume = p*l*t
  print("Luas Balok: ", luas, "\nVolume Balok:", volume)
elif pilihan == 3:
  r = int(input("Masukkan Jari-jari:"))
  phi = 3.14
  luas = 4 * phi * (r**2)
  volume = (4/3) * phi * (r**3)
  print("Luas Bola: ", luas, "\nVolume Bola: ", volume)
else:
  print("Pilihan Anda Tidak Ada")