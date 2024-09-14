usia = int(input("Masukkan usia: "))

if usia < 0:
    print("Input usia tidak valid")
elif usia <= 5:
    hargaTiket = 0
    print("Gratis")

else:
    keanggotaan = input("Apakah anda anggota (ya/tidak): ")
    if 5 <= usia <= 12:
        hargaTiket = 50000
    elif 13 <= usia <= 59:
        hargaTiket = 100000
    else:
        hargaTiket = 70000
    diskon = 0.2 if keanggotaan == 'ya' else 0
    hargaTiketSetelahDiskon = hargaTiket * (1 - diskon)
    
    print(f"Harga tiket setelah diskon: {hargaTiketSetelahDiskon:.2f}")