harga_tiket = int(input("Masukkan umur anda : "))

match harga_tiket:
    case h if h < 5:
        Kategori_harga:0
        print("Gratis")
        exit()
    case h if h >= 5 and h <= 12:
        keanggotaan = input("Apakah Anda anggota (ya/tidak): ").lower()
        Kategori_harga = 50000
    case h if h >= 13 and h <= 59:
        keanggotaan = input("Apakah Anda anggota (ya/tidak): ").lower()
        Kategori_harga = 100000 
    case _:
        keanggotaan = input("Apakah Anda anggota (ya/tidak): ").lower()
        Kategori_harga = 70000

anggota = Kategori_harga * 80//100 if keanggotaan == "ya" else Kategori_harga * 1

print(f"Harga tiket : Rp.{anggota:,}")

    