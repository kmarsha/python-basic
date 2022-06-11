print("===Penghitungan Gaji Karyawan===")

jam_kerja = int(input("Jumlah Jam Kerja:"))
jam_lembur = int(input("Jumlah Jam Lembur:"))
tidak_hadir = int(input("Jumlah Tidak Hadir:"))

total_gaji = (jam_kerja*15000) + (jam_lembur*10000) - (tidak_hadir*100000)

if total_gaji < 0:
  print("Ketidakhadiran membuat Anda tidak mendapat Gaji.")
else:
  print("Total Gaji:", total_gaji)

uang_makan = jam_kerja*10000

print("Uang makan:", uang_makan)