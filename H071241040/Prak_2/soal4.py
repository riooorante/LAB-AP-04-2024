#Soal 4
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
