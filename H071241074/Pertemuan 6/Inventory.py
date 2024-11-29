inventory = []

def input_angka(string):
    while True:
        try:
            return int(input(string))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def inputstr(str):
    while True:
        data = input(str)
        if data.strip() == "":
            print("input tidak valid")
        else:
            return data    

def tambah():
    kode = inputstr("Masukkan Kode barang: ")
    nama_barang = inputstr("Masukkan Nama barang: ")
    jumlah_barang = input_angka("Masukkan jumlah barang: ")
    harga_barang = input_angka("Masukkan Harga barang: ")
    barang = {"Kode": kode, "Nama": nama_barang, "Jumlah": jumlah_barang, "Harga": harga_barang}
    inventory.append(barang)

    print(f"{nama_barang} telah ditambahkan ke inventory.\n")

def hapus():
    kata_kunci = input("Masukkan kode atau nama barang yang ingin dihapus: ")
    for barang in inventory:
        if barang["Nama"] == kata_kunci or barang["Kode"] == kata_kunci:
            inventory.remove(barang)
            print(f"{kata_kunci} telah dihapus dari inventory.\n")
            return
    print(f"{kata_kunci} tidak ditemukan di inventory.\n")

def tampilkan():
    if not inventory:
        print("Inventory kosong.\n")
    else:
        print("Daftar Barang:")
        for barang in inventory:
            print(f"Kode: {barang['Kode']}, Nama: {barang['Nama']}, Jumlah: {barang['Jumlah']}, Harga: {barang['Harga']}")
        print()

def cari():
    kata_kunci = input("Masukkan kode atau nama barang yang ingin dicari: ")
    for barang in inventory:
        if barang["Nama"] == kata_kunci or barang["Kode"] == kata_kunci:
            print(f"Barang ditemukan: Kode: {barang['Kode']}, Nama: {barang['Nama']}, Jumlah: {barang['Jumlah']}, Harga: {barang['Harga']}\n")
            return
    print(f"{kata_kunci} tidak ditemukan di inventory.\n")


def update():
    kata_kunci = input("Masukkan kode atau nama barang yang ingin diupdate: ")
    for barang in inventory:
        if barang["Nama"] == kata_kunci or barang["Kode"] == kata_kunci:
            print("Pilih opsi update:\n1. Update jumlah\n2. Update harga\n3. Update jumlah dan harga")
            pilihan_update = input("Masukkan pilihan (1/2/3): ")
            
            if pilihan_update == '1':
                jumlah_baru = input_angka(f"Masukkan jumlah baru untuk {kata_kunci}: ")
                barang["Jumlah"] = jumlah_baru
                print(f"Jumlah untuk {kata_kunci} telah diperbarui.\n")
            elif pilihan_update == '2':
                harga_baru = input_angka(f"Masukkan harga baru untuk {kata_kunci}: ")
                barang["Harga"] = harga_baru
                print(f"Harga untuk {kata_kunci} telah diperbarui.\n")
            elif pilihan_update == '3':
                jumlah_baru = input_angka(f"Masukkan jumlah baru untuk {kata_kunci}: ")
                harga_baru = input_angka(f"Masukkan harga baru untuk {kata_kunci}: ")
                barang["Jumlah"] = jumlah_baru
                barang["Harga"] = harga_baru
                print(f"Jumlah dan harga untuk {kata_kunci} telah diperbarui.\n")
            else:
                print("Pilihan tidak valid.\n")
            return
    print(f"{kata_kunci} tidak ditemukan di inventory.\n")


while True:
    print("Menu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        hapus()
    elif pilihan == '3':
        tampilkan()
    elif pilihan == '4':
        cari()
    elif pilihan == '5':
        update()
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.\n")