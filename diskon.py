print("===Menghitung Diskon===")

belanja = int(input("Total Belanja:"))

if belanja >= 1500000:
  diskon = (10/100) * belanja
  bayar = belanja - diskon
  print("Kamu mendapat diskon 10% \nUang yang harus dibayar:", int(bayar))
elif belanja >= 1000000 and belanja <= 1500000:
  diskon = (5/100) * belanja
  bayar = belanja - diskon
  print("Kamu mendapat diskon 5% \nUang yang harus dibayar:", int(bayar))
elif belanja >= 500000 and belanja <= 1000000:
  diskon = (2/100) * belanja
  bayar = belanja - diskon
  print("Kamu mendapat diskon 2% \nUang yang harus dibayar:", int(bayar))
else:
  print("Kamu tidak mendapat diskon!")