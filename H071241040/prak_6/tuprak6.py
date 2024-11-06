inventory = {}  
def tambah_barang():  
    try:
        print("=== Tambah Barang ===")  
        id = int(input("Masukkan ID Barang: "))  
        if id in inventory:
            raise ValueError("ID barang sudah ada, gunakan ID yang berbeda.")
        nama = input("Masukkan Nama Barang: ") 
        for i in inventory.values(): 
            if i["nama"] == nama:
                raise ValueError("nama barang sudah ada, gunakan nama yang berbeda.")
        jumlah = int(input("Masukkan Jumlah Barang: "))  
        harga = int(input("Masukkan Harga Barang: "))
        inventory[id] = {"nama": nama, "jumlah": jumlah, "harga": harga}  
        print("Barang berhasil ditambahkan!")  
    except ValueError as e:
        print(f"Masukkan angka yang valid. Erorr: {e}")
def hapus_barang():  
    print("=== Hapus Barang ===")  
    try:
        id = int(input("Masukkan ID Barang yang ingin dihapus: "))
        if id in inventory:  
            del inventory[id]  
            print("Barang berhasil dihapus!")  
        else:  
            print("ID Barang tidak ditemukan!")  
    except ValueError as e:
        print(f"Error {e}")

def tampilkan_daftar_barang():  
    print("=== Daftar Barang ===")  
    if not inventory:  
        print("Tidak ada barang dalam inventory.")  
    else:  
        for i in inventory:  
            print(f"ID: {i}, Nama: {inventory[i]['nama']}, Jumlah: {inventory[i]['jumlah']}, Harga: {inventory[i]['harga']}")  

def cari_barang():  
    print("=== Cari Barang ===")  
    try:
        id = int(input("Masukkan ID Barang yang ingin dicari: "))
        if id in inventory:  
            data = inventory[id]  
            print(f"ID: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")  
        else:  
            print("ID Barang tidak ditemukan!") 
    except ValueError as e:
        print(f"Error {e}") 


def update_barang():  
    print("=== Update Data Barang ===")  
    try:
        id = int(input("Masukkan ID Barang yang ingin diupdate: "))  
        if id in inventory:  
            nama_baru = input("Masukkan Nama Barang baru (kosongkan jika tidak ingin mengubah): ")  
            jumlah_baru = input("Masukkan Jumlah Barang baru (kosongkan jika tidak ingin mengubah): ")  
            harga_baru = input("Masukkan Harga Barang baru (kosongkan jika tidak ingin mengubah): ")  

            if nama_baru != "":  
                inventory[id]["nama"] = nama_baru  
            if jumlah_baru != "":  
                inventory[id]["jumlah"] = jumlah_baru  
            if harga_baru != "":  
                inventory[id]["harga"] = harga_baru  
            print("Data barang berhasil diupdate!")  
        else:  
            print("ID Barang tidak ditemukan!")  
    except ValueError as e:
        print(f"Error {e}")
def tampilkan_menu():  
    print("=== Menu Inventory Barang ===")  
    print("1. Tambah Barang")  
    print("2. Hapus Barang")  
    print("3. Tampilkan Daftar Barang")  
    print("4. Cari Barang")  
    print("5. Update Data Barang")  
    print("6. Keluar")  
def main():  
    while True:  
        tampilkan_menu()  
        try:
            opsi = int(input("Pilih opsi (1-6): "))  
            if opsi == 1:  
                tambah_barang()  
            elif opsi == 2:  
                hapus_barang()  
            elif opsi == 3:  
                tampilkan_daftar_barang()  
            elif opsi == 4:  
                cari_barang()  
            elif opsi == 5:  
                update_barang()  
            elif opsi == 6:  
                print("Terima kasih! Program selesai.")  
                break  
            else:  
                print("Opsi tidak valid! Silakan pilih lagi.")  
        except ValueError :
            print("Masukkan Angka yang valid")


main()