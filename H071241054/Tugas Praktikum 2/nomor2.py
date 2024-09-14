#nomor 2
#input dari pengguna
usia = int(input("Masukkan usia= "))

if usia <= 0:
  print("Usia tidak valid")

elif 1 <= usia < 5:
  Harga_tiket = "Gratis"
  print(f"Harga tiket: {Harga_tiket}")

else: 
  anggota = input("Apakah anda anggota atau tidak?(ya/tidak): ")

  if 5 <= usia <= 12:
    Harga_tiket = 50000
  elif 13 <= usia <= 59:
    Harga_tiket = 100000
  else:
    Harga_tiket = 70000

  harga_akhir = Harga_tiket-(Harga_tiket*20/100) if anggota=="ya" else Harga_tiket

  print(f"Harga tiket: Rp{harga_akhir}")