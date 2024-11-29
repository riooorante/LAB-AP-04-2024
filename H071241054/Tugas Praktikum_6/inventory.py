inventory = {}

def tambah_barang(kode, nama, jumlah, harga):
    if kode in inventory:
        return "Kode barang sudah ada. Silakan gunakan kode yang berbeda."

    for item in inventory.values():
        if item['Nama barang'].lower() == nama.lower():
            return "Nama barang sudah ada. Silakan gunakan nama yang berbeda."

    inventory[kode] = {
        'Nama barang': nama,
        'Jumlah barang': jumlah,
        'Harga': harga
    }
    return "Barang berhasil ditambahkan."

def hapus_barang(kode):
    if kode in inventory:
        del inventory[kode]
        return "Barang berhasil dihapus."
    else:
        return "Barang tidak ditemukan."
    
def tampilkan_barang():
    if not inventory:
        return "Inventory kosong."
    
    tampilan = "Daftar Barang:\n"
    for kode, item in inventory.items():
        tampilan += (f"Kode barang: {kode}, "
                   f"Nama barang: {item['Nama barang']}, "
                   f"Jumlah barang: {item['Jumlah barang']}, "
                   f"Harga: {item['Harga']}\n")
    return tampilan
    
def cari_barang(pencarian):
    if pencarian == 1:          #mencari berdasarkan kode
        kode = input("Masukkan kode barang: ")
        if kode in inventory:
            item = inventory[kode]
            tampilkan = f"Nama barang: {item['Nama barang']}, Kode barang: {kode}, Jumlah barang: {item['Jumlah barang']}, Harga barang: {item['Harga']}"
            return tampilkan
        else:
            return "Barang tidak ditemukan."
    
    elif pencarian == 2:        #mencari berdasarkan nama
        nama = input("Masukkan nama barang: ").lower()
        for kode, item in inventory.items():
            if item['Nama barang'].lower() == nama:
                tampilkan = f"Nama barang: {item['Nama barang']}, Kode barang: {kode}, Jumlah barang: {item['Jumlah barang']}, Harga barang: {item['Harga']}"
                return tampilkan
        else:
            return "Barang tidak ditemukan."
        
    else:
        return "Pilihan tidak valid."

def update_barang(kode):
    if kode in inventory:
        item = inventory[kode]
        jumlah_baru = input("Masukkan jumlah baru: ")
        if jumlah_baru == " ":
            return "Input harga tidak valid. Harap masukkan angka."
        else:
            try:
                item['Jumlah barang'] = int(jumlah_baru)
            except ValueError:
                return "Input jumlah tidak valid. Harap masukkan angka."

        harga_baru = input("Masukkan harga barang baru: ")
        if jumlah_baru == " ":
            return "Input harga tidak valid. Harap masukkan angka."
        else:
            try:
                item['Harga'] = float(harga_baru)
                if item['Harga'] == " ":
                    return "Input harga tidak valid. Harap masukkan angka."
            except ValueError:
                return "Input harga tidak valid. Harap masukkan angka."

        inventory[kode] = item
        return f"Barang dengan kode {kode} berhasil diperbaharui."
    else:
        return f"Barang dengan kode {kode} tidak ditemukan."


while True:
    print("\n=== Menu Inventory Barang ===")
    pilihan = ["1. Tambah barang", "2. Hapus barang", "3. Tampilkan barang", "4. Cari barang", "5. Update barang", "6. Keluar  "]
    for i in pilihan:
        print(i)

    opsi = input("Pilih opsi (1-6): ")
    if opsi == "1":
        try:
            kode = input("Masukkan kode barang: ")
            nama = input("Masukkan nama barang: ").lower()
            jumlah = int(input("Masukkan jumlah barang: "))
            harga = float(input("Masukkan harga per unit: "))
            print(tambah_barang(kode, nama, jumlah, harga))
        except ValueError:
            print(f"Input tidak valid. Harap masukkan angka untuk jumlah/harga.")

    elif opsi == "2":
        kode = input("Masukkan kode barang yang akan dihapus: ")
        print(hapus_barang(kode))

    elif opsi == "3":
        print(tampilkan_barang())

    elif opsi == "4":
        try:
            pencarian = int(input("Cari berdasarkan (1) kode / (2) nama: "))
            print(cari_barang(pencarian))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka 1(kode)/2(nama).")

    elif opsi == "5":
        kode = input("Masukkan kode barang yang ingin diupdate: ")
        print(update_barang(kode))

    elif opsi == "6":
        print("Anda keluar.")
        break

    else:
        print("Pilihan hanya angka dalam rentang 1-6.")