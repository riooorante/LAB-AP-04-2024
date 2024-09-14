usia = int(input("Masukkan usia : "))

if 0 > usia :
    print("Usia tidak valid")
elif usia < 5 :
    print("Harga tiket: Gratis")
else :
    anggota = input("Apakah anda anggota (ya/tidak): ").lower()
    if 5 <= usia <= 12 :
        harga = 50000
    elif 13 <= usia <= 59 :
        harga = 100000
    else :
        harga = 70000

        harga_akhir = harga * 0.8 if anggota == "ya" else harga
        print(f'Harga tiket: Rp. {harga_akhir:.0f}')