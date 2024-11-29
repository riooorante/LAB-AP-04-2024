inventory = {}

while True:
    print("\n=== Menu Inventory Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Barang")
    print("4. Cari Barang")
    print("5. Update Barang")
    print("6. Keluar")

    pilihan = input("Pilih opsi (1-6): ")

    if pilihan == "1":
        while True:    
            kode = input("Masukkan kode barang: ")
            if kode.strip():
                break
            print("Input kosong. Silahkan coba lagi!")

        while True:
            nama = input("Masukkan nama barang: ")
            if nama.strip():
                break
            print("Input kosong. Silahkan coba lagi!")
       
        while True:
            try:
                jumlah = int(input("Masukkan jumlah barang: "))
                break
            except ValueError:
                print("Input tidak valid. Silahkan coba lagi!")

        while True:     
            try:
                harga = float(input("Masukkan harga per unit: "))
                break
            except ValueError:
                print("Input tidak valid. Silahkan coba lagi!")

        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print(f"Barang {nama} berhasil ditambahkan.")

    elif pilihan == "2":
        kode = input("Masukkan kode barang yang ingin dihapus: ")
        if kode in inventory:
            del inventory[kode]
            print(f"Barang dengan kode {kode} berhasil dihapus.")
        else:
            print(f"Barang dengan kode {kode} tidak ditemukan.")

    elif pilihan == "3":
        if inventory:
            print("\n=== Daftar Barang ===")
            for kode, info in inventory.items():
                print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
        else:
            print("Tidak ada barang di inventory.")

    elif pilihan == "4":
        if inventory:
            cari = input("Cari berdasarkan (1) Kode atau (2) Nama: ")
            if cari == "1":
                kode = input("Masukkan kode barang: ")
                if kode in inventory:
                    info = inventory[kode]
                    print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
                else:
                    print(f"Barang dengan kode {kode} tidak ditemukan.")
            elif cari == "2":
                nama = input("Masukkan nama barang: ").lower()
                ditemukan = False
                for kode, info in inventory.items():
                    if info['nama'].lower() == nama:
                        print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
                        ditemukan = True
                if not ditemukan:
                    print(f"Barang dengan nama {nama} tidak ditemukan.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Tidak ada barang di inventory.")

    elif pilihan == "5":
        kode = input("Masukkan kode barang yang ingin diupdate: ")
        if kode in inventory:
            info = inventory[kode]
            print(f"Data sebelumnya: Jumlah: {info['jumlah']}, Harga: {info['harga']}")

            jumlah_baru = input("Masukkan jumlah barang baru: ")
            if jumlah_baru:
                info['jumlah'] = int(jumlah_baru)  

            harga_baru = input("Masukkan harga barang baru: ")
            if harga_baru:
                info['harga'] = float(harga_baru) 

            inventory[kode] = info

            print(f"Data barang dengan kode {kode} berhasil diperbarui.")
        else:
            print(f"Barang dengan kode {kode} tidak ditemukan.")

    elif pilihan == "6":
        print("Terima kasih telah menggunakan program inventori!")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")