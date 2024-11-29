import os
from datetime import datetime

folder_film = "folder_film"
folder_tiket = "folder_tiket"

os.makedirs(folder_film, exist_ok=True)
os.makedirs(folder_tiket, exist_ok=True)

def get_film_file_path():
    return os.path.join(folder_film, "daftar_film.txt")

def menu_utama():
    while True:
        print(3 * "-", "Sistem Pemesanan Tiket Bioskop", 3 * "-")
        options = ["1. Admin", "2. Pengunjung", "3. Keluar"]
        print("\n".join(options))

        peran = input("Pilih peran (1/2/3): ")
        if peran == "1":
            menu_admin()
        elif peran == "2":
            menu_pengunjung()
        elif peran == "3":
            print("Terima kasih telah menggunakan sistem pemesanan tiket bioskop!")
            break
        else:
            print("Opsi tidak valid, silakan pilih kembali.")

def menu_admin():
    while True:
        print(3 * "-", "Menu Admin", 3 * "-")
        options = ["1. Tambah film", "2. Hapus film", "3. Daftar Tiket", "4. Kembali"]
        print("\n".join(options))
        opsi = input("Pilih opsi (1/2/3/4): ")

        if opsi == "1":
            tambah_film()
        elif opsi == "2":
            hapus_film()
        elif opsi == "3":
            daftar_tiket()
        elif opsi == "4":
            break
        else:
            print("Input tidak valid.")

def tambah_film():
    film = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
    if film:
        with open(get_film_file_path(), "a") as file:
            file.write(film + "\n")
        print(f"Film '{film}' ditambahkan ke file daftar film.")
    else:
        print("Input film kosong, kembali ke menu.")

def hapus_film():
    print("Daftar Film:")
    try:
        with open(get_film_file_path(), "r") as file:
            nama_film = file.readlines()
        for index, line in enumerate(nama_film, start=1):
            print(f"{index}. {line.strip()}")

        nomor_baris = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
        if nomor_baris == 0:
            return
        if 1 <= nomor_baris <= len(nama_film):
            del nama_film[nomor_baris - 1]
            with open(get_film_file_path(), "w") as file:
                file.writelines(nama_film)
            print("Film telah dihapus dari daftar.")
        else:
            print("Nomor baris tidak valid.")
    except (ValueError, IndexError):
        print("Input tidak valid. Harap masukkan angka untuk nomor film.")

def daftar_tiket():
    while True:
        print(3 * "-", "Daftar Tiket", 3 * "-")
        options = ["1. Lihat Daftar Tiket", "2. Lihat Detail Tiket", "3. Hapus Tiket", "4. Kembali"]
        print("\n".join(options))
        opsi = input("Pilih opsi (1/2/3/4): ")

        if opsi == "1":
            lihat_daftar_tiket()
        elif opsi == "2":
            lihat_detail_tiket()
        elif opsi == "3":
            hapus_tiket()
        elif opsi == "4":
            break
        else:
            print("Input tidak valid.")

def lihat_daftar_tiket():
    try:
        tiket_files = os.listdir(folder_tiket)
        if not tiket_files:
            print("Tidak ada tiket yang tersedia.")
        else:
            for index, id_tiket in enumerate(tiket_files, start=1):
                print(f"{index}. {id_tiket}")
    except Exception as e:
        print(f"Error! Tidak dapat membaca daftar tiket: {e}")

def lihat_detail_tiket():
    try:
        print("---Daftar tiket---")
        lihat_daftar_tiket()
        
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dilihat detailnya: "))
        file_tiket = os.listdir(folder_tiket)
        if 1 <= nomor_tiket <= len(file_tiket):
            tiket_file_path = os.path.join(folder_tiket, file_tiket[nomor_tiket - 1])
            with open(tiket_file_path, "r") as file:
                detail_tiket = file.read()
            print(f"Detail Tiket:\n{detail_tiket}")
        else:
            print(f"Tiket dengan nomor {nomor_tiket} tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor tiket.")

def hapus_tiket():
    try:
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dihapus: "))
        file_tiket = os.listdir(folder_tiket)
        if 1 <= nomor_tiket <= len(file_tiket):
            tiket_file_path = os.path.join(folder_tiket, file_tiket[nomor_tiket - 1])
            os.remove(tiket_file_path)
            print(f"Tiket nomor {nomor_tiket} telah dihapus.")
        else:
            print("Nomor tiket tidak valid.")
    except (ValueError, FileNotFoundError):
        print("Input tidak valid. Harap masukkan angka untuk nomor tiket.")

def menu_pengunjung():
    while True:
        print(3 * "-", "Menu Pengunjung", 3 * "-")
        options = ["1. Lihat daftar film", "2. Beli tiket", "3. Kembali"]
        print("\n".join(options))
        opsi = input("Pilih opsi (1/2/3): ")

        if opsi == "1":
            daftar_film()
        elif opsi == "2":
            beli_tiket()
        elif opsi == "3":
            break
        else:
            print("Input tidak valid.")

def daftar_film():
    try:
        with open(get_film_file_path(), "r") as file:
            nama_film = file.readlines()
        print("Daftar film:")
        for index, line in enumerate(nama_film, start=1):
            print(f"{index}. {line.strip()}")
    except Exception as e:
        print(f"Error! Daftar film tidak ditemukan: {e}")

def beli_tiket():
    daftar_film()
    print("0. Kembali")
    try:
        nomor_film = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
        if nomor_film == 0:
            return
        with open(get_film_file_path(), "r") as file:
            nama_film = file.readlines()
        if 1 <= nomor_film <= len(nama_film):
            film = nama_film[nomor_film - 1].strip()
            tiket_id = buat_tiket()
            tiket_info = detail_tiket(film, tiket_id)
            simpan_tiket(tiket_info, tiket_id)
            print(f"Tiket berhasil dibuat dengan ID: {tiket_id}")
        else:
            print(f"Nomor film {nomor_film} tidak ditemukan")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor film.")

def buat_tiket():
    now = datetime.now()
    return now.strftime("TICK%d%m%Y%H%M%S") + "!"

def detail_tiket(film, tiket_id):

    tiket_id_str = f"ID TICKET: {str(tiket_id)}".ljust(47) + "|"
    film_str = f"Film: {str(film)}".ljust(47) + "|"
    tanggal_str = f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".ljust(47) + "|"
    
    return f"""
+------------------------------------------------+
|                TIKET BIOSKOP                   |
| {tiket_id_str}
| {film_str}
| {tanggal_str}
+------------------------------------------------+
|       Terimakasih telah membeli tiket          |
|          Selamat menikmati filmnya             |
+------------------------------------------------+
"""

def simpan_tiket(tiket_info, tiket_id):
    tiket_file_path = os.path.join(folder_tiket, f"{tiket_id}.txt")
    try:
        with open(tiket_file_path, "w") as file:
            file.write(tiket_info)
        print(f"Tiket disimpan di {tiket_file_path}.")
    except Exception as e:
        print(f"Error! Tidak dapat menyimpan tiket: {e}")

menu_utama()
