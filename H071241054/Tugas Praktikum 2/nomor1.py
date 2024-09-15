#nomor 1
#input dari pengguna
a = int(input("Masukkan panjang sisi pertama= "))
b = int(input("Masukkan panjang sisi kedua= "))
c = int(input("Masukkan panjang sisi ketiga= "))

if a <= 0 or b <= 0 or c <= 0:
  print("Inputan tidak valid")
elif a + b <= c or a + c <= b or b + c <= a:
  print("Tidak dapat membentuk segitiga yang valid")
elif a == b == c:
  print("Segitiga Sama Sisi")
elif a == b or a == c or b == c:
  print("Segitiga Sama Kaki")
else:
  print("Segitiga Sembarang")