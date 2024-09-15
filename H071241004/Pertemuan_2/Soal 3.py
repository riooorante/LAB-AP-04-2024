a = int(input("Masukkan nilai akhir: "))
if (a > 100):
    print("Nilai tidak boleh di atas 100")
elif (a < 0):
    print("Nilai tidak boleh di bawah 0")
else:
    kehadiran = int(input("Masukkan persentase kehadiran: "))
    if (a >= 85) and (a <= 100):
        nilai = 'A'
    elif (a >= 70) and (a <= 84):
        nilai = 'B'
    elif (a >= 60) and (a <= 69):
        nilai = 'C'
    else:
        nilai = 'Tidak Lulus'

    if kehadiran >= 75 :
            if nilai == 'Tidak Lulus':
                b = int(input("Nilai tugas tambahan: "))
                if b > 70 :
                    print("Lulus dengan Predikat C")
                else:
                    print("Tidak lulus") 
            else:
                print(f"Lulus dengan Predikat {nilai}")
    else:
            print("Tidak lulus")