a = int(input("Masukkan usia: "))
if (a < 0):
    print("Inputan tidak valid")
elif (a < 5):
    print("Harga tiket: Gratis")
else:
    b = input("Apakah Anda anggota (ya/tidak): ")

    if (a <= 12):
        harga = 50000
    elif (a <= 59):
        harga = 100000
    else:
        harga = 70000

    harga_akhir = harga*0.8 if b == "ya" else harga
    print(f"Harga tiket: Rp.{harga_akhir:.0f}")