nilai = float(input("Masukkan nilai akhir: "))


if 0 <= nilai <= 100 :
    kehadiran = int(input("Masukkan presentase kehadiran: "))
    if nilai > 75: 
        print("Tidak lulus")
    elif nilai >= 85 :
        print("Lulus dengan Predikat A")
    elif nilai >= 70 :
        print("Lulus dengan Predikat B")
    elif nilai >= 60 :
        print("Lulus dengan Predikat C")
    else :
        tugas_tambahan = int(input("Nilai rata-rata tugas tambahan: ")) 
        if tugas_tambahan > 70 :
            print("Lulus dengan Predikat C") 
        else :
            print("Tidak lulus")
else: 
    print("Tidak valid")
    