data = {}

def tambah():
    kode = input("Masukkan kode barang : ")
    while True:
        try:
            nama = input("Masukkan nama barang : ")
            jumlah = int(input("Masukkan jumlah barang : "))
            harga = float(input("Masukkan harga barang per unit : "))
            break
        except:
            print("Mohon masukkan data dengan benar")

    data[kode] = {"kode" :  kode, "nama" : nama, "jumlah" : jumlah, "harga" : harga}
    print("Data berhasil ditambahkan")

def hapus():
    kode = input("Masukkan kode barang yang akan dihapus : ")

    if kode in data:
        del data[kode]
        print("Barang berhasil dihapus")
    else:
        print("Kode barang tidak ditemukan")

def tampilan():
    print("\nDaftar Barang :")
    for kode, barang in data.items():
        print(f"Kode : {kode}, Nama : {barang['nama']}, Jumlah : {barang['jumlah']},  Harga : {barang['harga']}")

def cari(kode):

    if kode in data:
        barang =  data[kode]
        print(f"Kode : {kode}, Nama : {barang['nama']}, Jumlah : {barang['jumlah']},  Harga : {barang['harga']}")
    else:
        print("Kode barang tidak ditemukan")

def perbarui():
    kode = input("Masukkan kode barang yang ingin diperbarui : ")

    if kode in data:
        cari(kode)
        barang = data[kode]
        jumlah = int(input("Masukkan jumlah baru: "))
        harga = float(input("Masukkan harga per unit baru : "))
        data[kode] = {"kode" : kode, "nama" : barang['nama'],
                      "jumlah" : jumlah, "harga" : harga}
        print("Data berhasil diperbarui")
    else:
        print("Kode barang tidak ditemukan")

def eksekusi():
    while True:
        print("\nMenu :")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Perbarui Barang")
        print("6. Keluar")
        pilihan = input("Pilih Menu (1-6) : ")

        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            hapus()
        elif pilihan == '3':
            tampilan()
        elif pilihan == '4':
            kode = input("Masukkan kode barang yang ingin dicari : ")
            cari(kode)
        elif pilihan == '5':
            perbarui()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan yang tidak sesuai, mohon masukkan piihan yang benar")

eksekusi()