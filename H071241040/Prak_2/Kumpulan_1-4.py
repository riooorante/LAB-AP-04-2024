# #Soal 1
# a = float(input("Masukkan panjang sisi pertama : "))
# b = float(input("Masukkan panjang sisi kedua : "))
# c = float(input("Masukkan panjang sisi ketiga : "))
# if a <= 0 or b <= 0 or c <= 0:
#     print("Inputan tidak valid")
# elif a == b ==c  :
#     print("Segitiga sama sisi")
# elif a == b or c==b or a==c:
#     print("Segitiga sama kaki")
# elif a != b and b != c and a!=c:
#     print("Tidak dapat membentuk segitiga yang valid") if a+b >= c or a+c >=b or b+c>=a else print("Segitiga sembarang")

# #Soal 2

# U5_12 = 50000
# U13_59 = 100000
# U60_ = 70000 
# persen= 0.8

# Usia = int(input("Masukkan Usia Anda : "))
# if Usia <= 0 :
#     print("Usia tidak Valid")
#     exit()
# elif  Usia < 5 :
#     print(f"Anda Gratis Masuk")
#     exit()

# anggota = input("Apakah Anda anggota [y/n]: ")
# if 5<Usia<12 :
#     print(f"Harga Tiket:Rp{U5_12*persen:,}") if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U5_12:,}")
# elif 13<U13_59<59 :
#     print(f"Harga TIket: Rp{U13_59*persen:,}")if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U13_59}:,")
# else:
#     print(f"Harga TIket: Rp{U60_*persen:,}")if anggota == "y" or anggota == "Y" else print(f"harga tiket: {U60_:,}")

# #Soal 3
# Nilai_akhir = int(input("Masukkan Nilai Akhir :"))
# if Nilai_akhir >100 or Nilai_akhir <=0:
#     print("Nilai akhir tidak Valid")
#     exit()
# kehadiran = int(input("Masukkan persentase kehadiran : "))
# if kehadiran < 75:
#     print("Anda Tidak Lulus")
#     exit()
# match Nilai_akhir:
#     case Nilai_akhir if 85<=Nilai_akhir<=100:
#         print("Lulus dengan predikat A")
#     case Nilai_akhir if 70<= Nilai_akhir<=84:
#         print("Lulus dengan predikat B")
#     case Nilai_akhir if 60<= Nilai_akhir<=69:
#         print("Lulus dengan predikat C")
#     case Nilai_akhir if Nilai_akhir < 60:
#         nilai = int(input("Nilai Tugas Tambahan : "))
#         if nilai > 70 :
#             print("Lulus dengan predikat C")
#         else:
#             print("Anda Tidak Lulus")

        
# soal 4


Jumlah_data = int(input("Jumlah data yang digunakan (GB) : "))
print("\noff peak = Penggunaan data antara jam 11 malam hingga 7 pagi")
print("peak =  Penggunaan data di luar jam 11 malam hingga 7 pagi\n")
waktu_penggunaan = input("Apakah penggunaan di luar jam sibuk (off peak) [y/n] ? : ")
print("\nPengguna Personal: Menggunakan internet untuk keperluan sehari-hari seperti browsing, streaming, dan media sosial. ")
print("Pengguna Bisnis: Menggunakan internet untuk keperluan bisnis seperti video conference, hosting website, dan cloud services  \n")
pengguna = input("Apakah anda pengguna Personal [y/n]:")
match Jumlah_data:
    case jumlah_data if Jumlah_data < 10 :
        if waktu_penggunaan == "y" and pengguna == "y":
            print("Paket yang sesuai: paket A")
        else:
            print("Tidak ada paket yang cocok")
    case jumlah_data if 10<=jumlah_data<50:
        if waktu_penggunaan == "n" and pengguna == "y":
            print("Paket yang sesuai: paket B ")
        else:
            print("Tidak ada paket yang cocok")
    case jumlah_data if jumlah_data>50:
       
        if  waktu_penggunaan == "y" and pengguna == "n":
            print("paket yang sesuai: paket D")
        elif waktu_penggunaan == "n" and pengguna == "y" or pengguna == "n":
            print("Paket yang sesuai: paket C")
        else:
            print("Tidak ada paket yang cocok")


# if Jumlah_data <10 and waktu_penggunaan == "y" and pengguna =="y":
#         paket = "A"
# elif 10 <= Jumlah_data <= 50 and waktu_penggunaan == "n" and pengguna =="y":
#         paket = "B"
# elif Jumlah_data > 50 and (waktu_penggunaan == "n" and pengguna =="n" or pengguna =="y"):
#         paket = "C"
# elif Jumlah_data> 50 and waktu_penggunaan == "y" and pengguna =="n":
#         paket = "D"
# else:
#         paket = "Tidak ada paket yang cocok"

# print("paket yang sesuai: ",paket)
    



