#Nomor 4
list = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
try:
    harga = int(input("Masukkan harga barang : ")) 
    bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
    kembalian = bayar - harga
    if harga > bayar :
        print(f"Anda Berhutang sebanyak {kembalian:,}")
        quit()
    print(f"Total Kembalian: Rp.{kembalian}")

    for i in list:
        count = kembalian // i 
        if count > 0 :
            print(f"{count} lembar Rp.{i:,}")
            kembalian = kembalian % i
        else:
            print(f"0 lembar Rp.{i:,}")
except ValueError:
    print("anda memasukan bukan angka")


  
