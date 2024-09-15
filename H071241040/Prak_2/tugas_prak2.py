# #Soal 2

# U5_12 = 50000
# U13_59 = 100000
# U60_ = 70000 
# persen= 0.8

# Usia = int(input("Masukkan Usia Anda : "))
# if Usia < 5 :
#     print(f"Anda Gratis Masuk")
#     exit()
# anggota = input("Apakah Anda anggota [y/n]: ")
# if 5<Usia<12 :
#     print(f"Harga Tiket:Rp{U5_12*persen:,}") if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U5_12:,}")
# elif 13<U13_59<59 :
#     print(f"Harga TIket: Rp{U13_59*persen:,}")if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U13_59}:,")
# else:
#     print(f"Harga TIket: Rp{U60_*persen:,}")if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U60_:,}")

#Soal 3
Nilai_akhir = int(input("Masukkan Nilai Akhir :"))
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
        nilai = int(input("Nilai Tugas Tambahan"))
        if nilai > 70 :
            print("Lulus dengan predikat C")
        else:
            print("Anda Tidak Lulus")
        