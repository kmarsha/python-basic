# rumus imt = bb/(tb**2)

# berat = 75 # kg
# tinggi = 1.75 # meter

berat = input("Masukkan Berat Badan:")
tinggi = input("Masukkan Tinggi Badan:")
usia = input("Masukkan Usia:")
jk = input("Masukkan Jenis Kelamin (l/p):")

imt = int(berat)/float(tinggi)**2

# print(berat/tinggi**2) # print langsung 
print("IMT kamu =", imt)

if jk == 'p':
  if imt <= 16.4:
    print("Kategori kamu kurus")
  elif imt <= 29.3 and imt >= 16.4:
    print("Kategori kamu normal")
  elif imt >= 29.3:
    print("Kategori kamu gemuk")

if jk == 'l':
  if imt <= 16.9:
    print("Kategori kamu kurus")
  elif imt <= 28.5 and imt >= 16.9:
    print("Kategori kamu normal")
  elif imt >= 28.8:
    print("Kategori kamu gemuk")