nilai_akhir = float(input("Masukkan nilai akhir: "))
if nilai_akhir >= 100:
    print("Input tidak valid")
    exit()
elif nilai_akhir <= 0:
    print("Input tidak valid")
    exit()

kehadiran = float(input("Masukkan presentase kehadiran: "))

if kehadiran >=  75:
    if nilai_akhir >= 85:
        predikat = "A"
    elif nilai_akhir >= 70:
        predikat = "B"
    elif nilai_akhir >= 60:
        predikat = "C"
    else:
        tugas = float(input("Masukkan nilai tugas tambahan: "))
        if tugas >= 70:
            predikat = "C"
        else:
            predikat = "tidak lulus"
else:
    predikat = "Tidak lulus"
    print(f"Predikat kelulusan: {predikat}")