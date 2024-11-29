import os
from datetime import datetime

# Global variabel untuk menyimpan data
daftar_film = []
daftar_tiket = {}

def generate_ticket_id():
    return "TICK" + datetime.now().strftime("%d%m%Y%H%M%S")


def detail_tiket(film, id_tiket):
    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    film_diproses = (film[:27] + '..') if len(film) > 27 else film.ljust(27)  # Memotong jika lebih dari 27 karakter
    detail = f"""
    +-----------------------------------+
    |        TIKET BIOSKOP              |
    | ID TICKET: {id_tiket.ljust(27)}   |
    | Film: {film_diproses}             |
    | Tanggal: {tanggal.ljust(27)}      |
    +-----------------------------------+
    |     Terimakasih telah membeli     |
    |            tiket anda             |
    +-----------------------------------+
    """
    return detail

    

# Admin: Tambah Film
def tambah_film():
    while True:
        nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if nama_film == "":
            break
        daftar_film.append(nama_film)
        print(f"Film '{nama_film}' berhasil ditambahkan.\n")

        # Membuat file untuk film yang baru ditambahkan
        if not os.path.exists("film"):
            os.makedirs("film")
        with open(f"film/{nama_film}.txt", "w") as file:
            file.write(f"Film: {nama_film}\n")
            file.write("Informasi tentang film ini akan ditambahkan kemudian.\n")
        print(f"File untuk film '{nama_film}' telah dibuat: film/{nama_film}.txt\n")

# Admin: Hapus Film
def hapus_film():
    while True:
        if len(daftar_film) == 0:
            print("Tidak ada film yang tersedia.")
            break
        print("--- Daftar Film ---")
        for idx, film in enumerate(daftar_film, 1):
            print(f"{idx}. {film}")
        print("0. Kembali")
        
        pilihan = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(daftar_film):
            film_dihapus = daftar_film.pop(pilihan - 1)
            print(f"Film '{film_dihapus}' berhasil dihapus.\n")

# Admin: Menampilkan Daftar Tiket
def daftar_tiket_admin():
    print("--- Daftar Tiket ---")
    if len(daftar_tiket) == 0:
        print("Belum ada tiket yang dibeli.\n")
    else:
        for idx, (id_tiket, tiket_info) in enumerate(daftar_tiket.items(), 1):
            print(f"{idx}. ID Tiket: {id_tiket} | Film: {tiket_info['film']} | Tanggal: {tiket_info['tanggal']}")

# Admin: Hapus Tiket
def hapus_tiket_admin():
    while True:
        if len(daftar_tiket) == 0:
            print("Belum ada tiket yang tersedia.")
            break
        print("--- Daftar Tiket ---")
        for idx, (id_tiket, tiket_info) in enumerate(daftar_tiket.items(), 1):
            print(f"{idx}. ID Tiket: {id_tiket} | Film: {tiket_info['film']} | Tanggal: {tiket_info['tanggal']}")
        print("0. Kembali")

        pilihan = int(input("Masukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(daftar_tiket):
            tiket_dihapus = list(daftar_tiket.keys())[pilihan - 1]
            del daftar_tiket[tiket_dihapus]
            os.remove(f"tickets/{tiket_dihapus}.txt")  # Menghapus file tiket
            print(f"Tiket dengan ID '{tiket_dihapus}' berhasil dihapus.\n")

# Pengunjung: Beli Tiket
def beli_tiket():
    if len(daftar_film) == 0:
        print("Belum ada film yang tersedia.\n")
        return
    print("--- Daftar Film ---")
    for idx, film in enumerate(daftar_film, 1):
        print(f"{idx}. {film}")
    print("0. Kembali")
    
    pilihan = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
    if pilihan == 0:
        return
    if 1 <= pilihan <= len(daftar_film):
        film_dipilih = daftar_film[pilihan - 1]
        id_tiket = generate_ticket_id()
        tanggal_beli = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        daftar_tiket[id_tiket] = {'film': film_dipilih, 'tanggal': tanggal_beli}
        
        print(f"Tiket berhasil dibeli. ID tiket Anda: {id_tiket}")
        
        # Simpan tiket ke file teks
        if not os.path.exists("tickets"):
            os.makedirs("tickets")
        with open(f"tickets/{id_tiket}.txt", "w") as file:
            file.write(f"TIKET BIOSKOP\n")
            file.write(f"ID Tiket  : {id_tiket}\n")
            file.write(f"Film      : {film_dipilih}\n")
            file.write(f"Tanggal   : {tanggal_beli}\n")
            file.write("Terima kasih telah membeli tiket Anda!\n")
        
        print(f"File tiket telah dibuat: tickets/{id_tiket}.txt\n")
        detail_tiket(film, id_tiket)

# Sistem Pemesanan Tiket
def sistem_pemesanan_tiket():
    while True:
        print("--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        peran = input("Pilih peran (1/2/3): ").strip()  # Mengambil input dan menghilangkan spasi kosong di awal dan akhir

        # Memeriksa apakah input kosong atau bukan angka yang valid
        if peran == "":
            print("Masukkan pilihan yang valid.\n")
            continue
        elif not peran.isdigit() or int(peran) not in [1, 2, 3]:
            print("Pilihan tidak valid. Masukkan angka 1, 2, atau 3.\n")
            continue

        peran = int(peran)
        
        if peran == 1:
            while True:
                print("--- Menu Admin ---")
                print("1. Tambah film")
                print("2. Hapus film")
                print("3. Daftar Tiket")
                print("4. Hapus Tiket")  
                print("5. Kembali")
                opsi_admin = input("Pilih opsi (1/2/3/4/5): ").strip()
                
                if opsi_admin == "":
                    print("Masukkan pilihan yang valid.\n")
                    continue
                elif not opsi_admin.isdigit() or int(opsi_admin) not in [1, 2, 3, 4, 5]:
                    print("Pilihan tidak valid. Masukkan angka 1, 2, 3, 4, atau 5.\n")
                    continue

                opsi_admin = int(opsi_admin)
                
                if opsi_admin == 1:
                    tambah_film()
                elif opsi_admin == 2:
                    hapus_film()
                elif opsi_admin == 3:
                    daftar_tiket_admin()
                elif opsi_admin == 4:
                    hapus_tiket_admin()
                elif opsi_admin == 5:
                    break
        
        elif peran == 2:
            while True:
                print("--- Menu Pengunjung ---")
                print("1. Lihat daftar film")
                print("2. Beli tiket")
                print("3. Kembali")
                opsi_pengunjung = input("Pilih opsi (1/2/3): ").strip()
                
                if opsi_pengunjung == "":
                    print("Masukkan pilihan yang valid.\n")
                    continue
                elif not opsi_pengunjung.isdigit() or int(opsi_pengunjung) not in [1, 2, 3]:
                    print("Pilihan tidak valid. Masukkan angka 1, 2, atau 3.\n")
                    continue

                opsi_pengunjung = int(opsi_pengunjung)
                
                if opsi_pengunjung == 1:
                    if len(daftar_film) == 0:
                        print("Belum ada film yang tersedia.\n")
                    else:
                        print("--- Daftar Film ---")
                        for idx, film in enumerate(daftar_film, 1):
                            print(f"{idx}. {film}")
                        print()
                elif opsi_pengunjung == 2:
                    beli_tiket() 
                elif opsi_pengunjung == 3:
                    break
        
        elif peran == 3:
            print("Terima kasih telah menggunakan sistem ini.")
            break

sistem_pemesanan_tiket()

