#Soal 3
Nilai_akhir = int(input("Masukkan Nilai Akhir :"))
if Nilai_akhir >100 or Nilai_akhir <=0:
    print("Nilai akhir tidak Valid")
    exit()
kehadiran = int(input("Masukkan persentase kehadiran : "))
if kehadiran < 75:
    print("Anda Tidak Lulus")
    exit()
match Nilai_akhir:
    case Nilai_akhir if 85<=Nilai_akhir<=100:
        print("Lulus dengan predikat A")
    case Nilai_akhir if 70<= Nilai_akhir<=84:
        print("Lulus dengan predikat B")
    case Nilai_akhir if 60<= Nilai_akhir<=69:
        print("Lulus dengan predikat C")
    case Nilai_akhir if Nilai_akhir < 60:
        nilai = int(input("Nilai Tugas Tambahan : "))
        if nilai > 70 :
            print("Lulus dengan predikat C")
        else:
            print("Anda Tidak Lulus")
