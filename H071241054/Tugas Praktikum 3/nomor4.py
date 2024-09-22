harga = int(input("Masukkan total harga: "))
pembayaran = int(input("Masukkan uang yang diberikan: "))

kembalian = pembayaran - harga
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if kembalian == 0:
    print("Tidak ada kembalian")
elif harga > pembayaran:
    print(f"Pembayaran belum lunas. Uang yang diberikan masih kurang Rp{abs(pembayaran - harga)}")
else:
    for i in pecahan_uang:
        if kembalian >= i:
            jumlah_lembaran = kembalian // i
            kembalian %= i
            print(f"{jumlah_lembaran} lembar Rp{i}")