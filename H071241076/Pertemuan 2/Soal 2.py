usia = int(input("Masukkan usia: "))

# Tentukan harga dasar berdasarkan usia
if usia <= 0:
    print("usia tidak valid")
elif 1<=usia<5:
    print("Harga tiket : Gratis")
else:
    anggota = input("Apakah Anda anggota (ya/tidak): ")
    if 5 <= usia <= 12:
        harga_dasar = 50000
    elif 13 <= usia <= 59:
        harga_dasar = 100000
    else:
        harga_dasar = 70000

    harga_akhir = harga_dasar - int(harga_dasar * 0.2 if anggota == 'ya' else 0)

    print("Harga tiket: Rp.", harga_akhir)