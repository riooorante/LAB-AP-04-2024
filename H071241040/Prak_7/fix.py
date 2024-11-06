import os
from datetime import datetime

# Template/deklarasi
kumpulan_film = "list_film"
lokasi_modul = f"{kumpulan_film}/list.txt"
tiket = "tikets"

def buat_folder_jika_tidak_ada(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def baca_file(lokasi):
    f = open(lokasi, 'r')
    lines = f.readlines()
    f.close()
    return lines

def tampilkan_menu_admin():
    print("--- Menu Admin ---")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Daftar Tiket")
    print("4. Keluar")

def tampilkan_menu_pengunjung():
    print("--- Menu Pengunjung ---")
    print("1. Lihat daftar film")
    print("2. Beli tiket")
    print("3. Kembali")

def tampilkan_menu_main():
    print("--- Sistem Pemesanan Tiket Bioskop ---")
    print("1. Admin")
    print("2. Pengunjung")
    print("3. Keluar")

def tambah_film():
    try:
        print("--- Tambah Film  ---")
        while True:
            buat_folder_jika_tidak_ada(kumpulan_film)
            nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali) : ")
            if nama_film == "":
                print("Kembali ke menu admin")
                break
            f = open(lokasi_modul, "a")
            f.write(f"{nama_film}\n")
            f.close()
            print(f"Film '{nama_film}' berhasil ditambahkan")
    except ValueError as e:
        print(f"Film ini invalid, Erorr: {e}")

def hapus_film():
    print("--- Hapus Film ---")
    try:
        while True:
            print("Daftar Film: ")
            buat_folder_jika_tidak_ada(kumpulan_film)
            list = os.listdir(kumpulan_film)
            if not list:
                print("Tidak ada tiket yang terpesan")
                return
            i = 1
            modul = baca_file(lokasi_modul)
            for line in modul:
                print(f"{i}. {line}")
                i += 1
            print("0. Kembali")
            nama_film = int(input("Masukkan nama film yang ingin dihapus (atau 0 untuk kembali) : "))
            if nama_film == 0:
                print("Kembali ke menu admin")
                break
            if 1 <= nama_film <= len(modul):
                del modul[nama_film - 1]
                f = open(lokasi_modul, 'w')
                f.writelines(modul)
                f.close()
                print(f"Film {nama_film} berhasil dihapus\n")
            else:
                print("Inputan Invalid")
    except ValueError as e:
        print(f"Error {e}")

def daftar_tiket():
    try:
        print("--- Daftar Tiket ---")
        buat_folder_jika_tidak_ada(tiket)
        list = os.listdir(tiket)
        if not list:
            print("Tidak ada tiket yang terpesan")
            return
        i = 1
        for k in list:
            file = os.path.splitext(k)[0]
            print(f"{i}. {file}")
            i += 1
        print("0. Keluar\n")
        pilih = int(input("Pilih nomor tiket yang ingin dilihat: "))
        if 1 <= pilih <= len(list):
            pilih_file = list[pilih - 1]
            tempat_file = os.path.join(tiket, pilih_file)
            file = open(tempat_file, 'r')
            content = file.read()
            file.close()
            print(content)
        else:
            print("Inputan Diluar jangkauan")
    except ValueError as e:
        print(e)

def admin():
    while True:
        tampilkan_menu_admin()
        try:
            opsi = int(input("Pilih opsi (1/2/3/4): "))
            if opsi == 1:
                tambah_film()
            elif opsi == 2:
                hapus_film()
            elif opsi == 3:
                daftar_tiket()
            elif opsi == 4:
                print("Kembali ke menu utama")
                break
            else:
                print("Opsi tidak valid! Silakan pilih lagi.")
        except ValueError:
            print("Masukkan Angka yang valid")

def daftar_film():
    i = 1
    buat_folder_jika_tidak_ada(kumpulan_film)
    list = os.listdir(kumpulan_film)
    if not list:
        print("Belum ada film yang tersedia")
        return
    modul = baca_file(lokasi_modul)
    print("Daftar Film: ")
    for line in modul:
        print(f"{i}. {line}")
        i += 1

def beli_tiket():
    try:
        buat_folder_jika_tidak_ada(kumpulan_film)
        list = os.listdir(kumpulan_film)
        if not list:
            print("Belum ada film yang tersedia")
            return

        nama = datetime.now().strftime("%d%m%Y%H%M%S")
        id_tiket = f"TIX{nama}"
        real_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        modul = baca_file(lokasi_modul)
        i = 1
        for line in modul:
            print(f"{i}. {line}")
            i += 1
        pilih = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali) :"))
        if 1 <= pilih <= len(modul):
            ambil = modul[pilih - 1].strip()
            if not os.path.exists(tiket):
                os.makedirs(tiket)
            Ljust = ambil.ljust(27)
            nama_file = (f"{tiket}/{id_tiket}.txt")
            f = open(f"{nama_file}", "w")
            f.write(f"""
+----------------------------------------+
|              TIKET BIOSKOP             |
+----------------------------------------+
| ID Tiket  : {id_tiket}          |
| Film      : {Ljust}|           
| Tanggal   : {real_time}        |
+----------------------------------------+
| Terima kasih telah membeli tiket Anda! |
+----------------------------------------+""")
            f.close()
            print(f"Tiket telah dibeli. ID tiket anda : {id_tiket}")
            print(f"File tiket telah dibuat :{nama_file} ")
        else:
            raise ValueError("Angka Diluar jangkauan")
    except ValueError as e:
        print(e)

def pengunjung():
    while True:
        tampilkan_menu_pengunjung()
        try:
            opsi = int(input("Pilih opsi (1/2/3): "))
            if opsi == 1:
                daftar_film()
            elif opsi == 2:
                beli_tiket()
            elif opsi == 3:
                print("Kembali ke menu utama")
                break
            else:
                print("Opsi tidak valid! Silakan pilih lagi.")
        except ValueError:
            print("Masukkan Angka yang valid")

def main_menu():
    while True:
        tampilkan_menu_main()
        try:
            opsi = int(input("Pilih peran (1/2/3): "))
            if opsi == 1:
                admin()
            elif opsi == 2:
                pengunjung()
            elif opsi == 3:
                print("Terima Kasih, Selamat datang kembali")
                break
            else:
                print("Opsi tidak valid! Silakan pilih lagi.")
        except ValueError:
            print("Masukkan Angka yang valid")
#Mulai
main_menu()
