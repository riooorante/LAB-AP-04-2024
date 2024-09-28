import random

kesempatan = 5
angkarahasia = random.randint(1, 100)



for i in range (kesempatan):
  a = int(input("Masukkan Angka : "))
  kesempatan -= 1
  if a == 0:
    print("Anda Berhenti Bermain")
    break
  if a == angkarahasia:
    print("Selamat Anda Menang")
    break

  elif a < angkarahasia:
    print("angka terlalu kecil")

  elif a > angkarahasia:
    print("angka terlalu besar")

  if kesempatan == 0:
    print("Anda Kalah")
