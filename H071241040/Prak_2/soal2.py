#Soal 2

U5_12 = 50000
U13_59 = 100000
U60_ = 70000 
persen= 0.8

Usia = int(input("Masukkan Usia Anda : "))
if Usia <= 0 :
    print("Usia tidak Valid")
    exit()
elif  Usia < 5 :
    print(f"Anda Gratis Masuk")
    exit()

anggota = input("Apakah Anda anggota [y/n]: ")
if 5<Usia<12 :
    print(f"Harga Tiket:Rp{U5_12*persen:,}") if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U5_12:,}")
elif 13<U13_59<59 :
    print(f"Harga TIket: Rp{U13_59*persen:,}")if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U13_59}:,")
else:
    print(f"Harga TIket: Rp{U60_*persen:,}")if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U60_:,}")
