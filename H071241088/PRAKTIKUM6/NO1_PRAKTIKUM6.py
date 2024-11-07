inventory = {}

def tambah_barang():
    try:
        kode = input("Masukkan kode barang: ")
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))
        harga = int(input("Masukkan harga barang: "))
        
        if kode in inventory:
            print("Barang dengan kode tersebut sudah ada!")
        else:
            inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
            print("Barang berhasil ditambahkan!")
    except ValueError:
        print("Input jumlah atau harga harus berupa angka! Silakan coba lagi.")

def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    
    if kode in inventory:
        del inventory[kode]
        print("Barang berhasil dihapus!")
    else:
        print("Barang dengan kode tersebut tidak ditemukan!")

def tampilkan_daftar_barang():
    if inventory:
        print("\nDaftar Barang di Gudang:")
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("\nGudang kosong.")

def cari_barang():
    kode = input("Masukkan kode barang yang ingin dicari: ")
    
    if kode in inventory:
        data = inventory[kode]
        print(f"Barang ditemukan: Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Barang dengan kode tersebut tidak ditemukan!")

def update_barang():
    try:
        kode = input("Masukkan kode barang yang ingin diupdate: ")
        
        if kode in inventory:
            nama = input("Masukkan nama barang baru: ")
            jumlah = int(input("Masukkan jumlah barang baru: "))
            harga = int(input("Masukkan harga barang baru: "))
            
            inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
            print("Data barang berhasil diupdate!")
        else:
            print("Barang dengan kode tersebut tidak ditemukan!")
    except ValueError:
        print("Input jumlah atau harga harus berupa angka! Silakan coba lagi.")

while True:
    print("\nMenu Inventory Barang:")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        hapus_barang()
    elif pilihan == '3':
        tampilkan_daftar_barang()
    elif pilihan == '4':
        cari_barang()
    elif pilihan == '5':
        update_barang()
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi!")