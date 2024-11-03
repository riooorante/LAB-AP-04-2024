inventory = {}

def menu():
    while True:
        print("\n======= Menu =======")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        opsi = input("Pilih Menu (1-6) : ")

        if opsi == '1':
            tambah_barang()
        elif opsi == '2':
            hapus_barang()
        elif opsi == '3':
            tampilkan_barang()
        elif opsi == '4':
            id = input("Masukkan id barang yang ingin dicari : ")
            cari_barang(id)
        elif opsi == '5':
            update_barang()
        elif opsi == '6':
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid, Harap pilih 1-6")

def tambah_barang():
    while True:
        try:
            id = input("Masukkan id barang : ")
            nama = input("Masukkan nama barang : ")
            jumlah = int(input("Masukkan jumlah barang : "))
            harga = float(input("Masukkan harga barang per unit : "))
            break
        except:
            print("Harap masukkan inventory dengan benar")

    inventory[id] = {"id" :  id, "nama" : nama, "jumlah" : jumlah, "harga" : harga}
    print("Data berhasil ditambahkan")

def hapus_barang():
    tampilkan_barang()
    id = input("Masukkan id barang yang akan dihapus : ")

    if id in inventory:
        del inventory[id]
        print("Barang berhasil dihapus")
    else:
        print("Kode barang tidak ditemukan")

def tampilkan_barang():
    print("\nDaftar Barang :")\
        
    for id, barang in inventory.items():
        print(f"Kode : {id}, Nama : {barang['nama']}, Jumlah : {barang['jumlah']},  Harga : {barang['harga']}")

def cari_barang(id):

    if id in inventory:
        barang =  inventory[id]
        print(f"Kode : {id}, Nama : {barang['nama']}, Jumlah : {barang['jumlah']},  Harga : {barang['harga']}")
    else:
        print("Kode barang tidak ditemukan")

def update_barang():
    tampilkan_barang()
    id = input("Masukkan id barang yang ingin diupdate : ")

    try:
        if id in inventory:
            cari_barang(id)
            barang = inventory[id]
            jumlah = int(input("Masukkan jumlah baru : "))
            harga = float(input("Masukkan harga per unit baru : "))
            inventory[id] = {"id" : id, "nama" : barang['nama'],
                        "jumlah" : jumlah, "harga" : harga}
            print("Data berhasil diupdate")
        else:
            print("Barang tidak ditemukan")
    except:
        print("Harap masukkan data dengan benar")

menu()