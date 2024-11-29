
inventory = []

def tambah_barang():
      try:
        nama = input("Masukkan nama barang: ")
        if not nama:
            raise ValueError("Nama barang tidak boleh kosong!")

        jumlah = int(input("Masukkan jumlah barang: "))
        if jumlah <= 0:
            raise ValueError("Jumlah barang harus lebih dari 0!")

        harga = float(input("Masukkan harga barang: "))


        inventory.append({
            'nama': nama,
            'jumlah': jumlah,
            'harga': harga
        })
        print("Barang berhasil ditambahkan ke inventory!")

      except ValueError as e:
        print(f"Error: {e}")



print("Inventory saat ini:", inventory)

def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")

    for barang in inventory:
        if barang['nama'].lower() == nama.lower():
            inventory.remove(barang)
            print(f"Barang '{nama}' berhasil dihapus!")
            return

    print(f"Barang '{nama}' tidak ditemukan!")

def tampilkan_barang():
    if not inventory:
        print("Tidak ada barang di dalam inventory.")
        return

    print("Daftar Barang di Inventory:")
    for index, barang in enumerate(inventory, start=1):
        print(f"{index}. Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

def cari_barang():
    nama = input("Masukkan nama barang yang ingin dicari: ")

    for barang in inventory:
        if barang['nama'].lower() == nama.lower():
            print(f"Barang ditemukan: Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
            return

    print(f"Barang '{nama}' tidak ditemukan!")


def update_barang():
    nama = input("Masukkan nama barang yang ingin diupdate: ")

    for barang in inventory:
        if barang['nama'].lower() == nama.lower():
            print(f"Data lama -> Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

            try:
                nama_barang =  input("Masukkan nama barang baru: ")
                print(nama_barang)
                if not barang:
                    raise ValueError("Nama barang tidak boleh kosong!")

                jumlah_barang = input("Masukkan jumlah barang baru: ")

                if not jumlah_barang.isdigit() or jumlah_barang.isalpha() or jumlah_barang.strip() == "" :
                    raise ValueError("Jumlah barang harus lebih dari 0!")

                harga_baru = input("Masukkan harga barang baru: ")

                if not jumlah_barang.isdigit() or jumlah_barang.isalpha() or jumlah_barang.strip() == "" :
                    raise ValueError("Masukkan harga yang valid!")

                print(f"Barang '{nama}' berhasil diupdate!")
                barang["nama"] = nama_barang

                barang['jumlah'] = int(jumlah_barang)
                barang['harga'] = float(harga_baru)
                return
            except ValueError as e:
                print(f"Error: {e}")
                return

    print(f"Barang '{nama}' tidak ditemukan!")

def menu():
    while True:
        print("\n=== Program Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Terima kasih! Program berakhir.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


menu()

