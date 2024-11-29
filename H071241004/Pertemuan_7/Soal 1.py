import time
import os

def pastikan_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def generate_ticket_id():
    return f"TICK{time.strftime('%d%m%Y%H%M%S')}"

def tambah_film(nama_film):
    pastikan_folder("film")
    with open(os.path.join("film", "daftar_film.txt"), "a") as file:
        file.write(f"{nama_film}\n")
    print(f"Film '{nama_film}' berhasil ditambahkan.")

def hapus_film():
    if not tampilkan_film():
        return print('Tidak ada data untuk dihapus!')
    nama_film = input("Masukkan nama film: ")
    file_path = os.path.join("film", "daftar_film.txt")
    with open(file_path, "r") as file:
        films = file.readlines()
    with open(file_path, "w") as file:
        for film in films:
            if film.strip() != nama_film:
                file.write(film)
            else:
                print(f"Film '{nama_film}' berhasil dihapus.")
                return
    print(f"Film '{nama_film}' tidak ditemukan.")

def tampilkan_film():
    try:
        with open(os.path.join("film", "daftar_film.txt"), "r") as file:
            films = file.readlines()
        if not films:
            print("Daftar film kosong.")
            return False
        print("Film yang tersedia:")
        for i, film in enumerate(films, 1):
            print(f"{i}. {film.strip()}")
        return True
    except FileNotFoundError:
        print("File daftar film tidak ditemukan.")
        return False

def beli_tiket():
    if not tampilkan_film():
        return
    nama_film = input("Masukkan judul film yang ingin dibeli : ")
    
    # Verifikasi film
    with open(os.path.join("film", "daftar_film.txt"), "r") as file:
        films = [film.strip() for film in file.readlines()]
    if nama_film not in films:
        print(f"Film '{nama_film}' tidak tersedia.")
        return

    ticket_id = generate_ticket_id()
    pastikan_folder("tiket")
    with open(os.path.join("tiket", f"{ticket_id}.txt"), "w") as file:
        file.write(f"Ticket ID: {ticket_id}\nFilm: {nama_film}")
    print(f"Tiket berhasil dibeli. ID: {ticket_id}, Film: {nama_film}")
    
def tampilkan_tiket():
    tickets = os.listdir("tiket")
    if not tickets:
        print("Tidak ada tiket yang dibeli.")
        return False
    print("Daftar tiket yang telah dibeli:")
    
    print(",".join(tickets))
    # for ticket in tickets:
    #     with open(os.path.join("tiket", ticket), "r") as file:
    #         print(file.read())
    #         print("-" * 30)
    # return True

def tampilkan_detail_tiket():
    if not tampilkan_tiket():
        return
    ticket_id = input("Masukkan ID tiket: ")
    try:
        with open(os.path.join("tiket", f"{ticket_id}.txt"), "r") as file:
            print("\nDetail tiket:")
            print(file.read())
    except FileNotFoundError:
        print(f"Tiket dengan ID '{ticket_id}' tidak ditemukan.")

def hapus_tiket():
    if not tampilkan_tiket():
        return
    ticket_id = input("Masukkan ID tiket yang ingin dihapus: ")
    try:
        os.remove(os.path.join("tiket", f"{ticket_id}.txt"))
        print(f"Tiket dengan ID '{ticket_id}' berhasil dihapus.")
    except FileNotFoundError:
        print(f"Tiket dengan ID '{ticket_id}' tidak ditemukan.")

def menu_admin():
    while True:
        print("\n", " Menu Admin ".center(60, '=').upper())
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Tampilkan Daftar Film")
        print("4. Tampilkan Semua Tiket")
        print("5. Tampilkan Detail Tiket")
        print("6. Hapus Tiket")
        print("7. Logout")

        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            nama_film = input("Masukkan nama film : ")
            if nama_film == '':
                print('Inputan tidak valid')
            else:
                tambah_film(nama_film)
        elif pilihan == "2":
            hapus_film()
        elif pilihan == "3":
            tampilkan_film()
        elif pilihan == "4":
            tampilkan_tiket()
        elif pilihan == "5":
            tampilkan_detail_tiket()
        elif pilihan == "6":
            hapus_tiket()
        elif pilihan == "7":
            print("Logout...")
            break
        else:
            print('Inputan tidak valid!')

def menu_pengunjung():
    while True:
        print("\n", " Menu Pengunjung ".center(60, '=').upper())
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("3. Logout")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            tampilkan_film()
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            print("Logout...")
            break
        else:
            print('Imputan tidak valid!')

def utama():
    while True:
        print("\n", " Selamat datang di SIB ".center(60, '=').upper())
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        peran = input("Pilih peran Anda: ")
        if peran == "1":
            menu_admin()
        elif peran == "2":
            menu_pengunjung()
        elif peran == "3":
            print("Keluar dari sistem.")
            break
        else:
            print('Inputan tidak valid!')

utama()