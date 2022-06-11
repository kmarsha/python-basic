print("===Bangun Datar===")
print("1. Persegi\n2. Persegi Panjang\n3. Jajargenjang")

pilihan_datar = int(input("Pilih Bangun Datar:"))

if pilihan_datar == 1:
  sisi = int(input("Masukkan Sisi"))
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