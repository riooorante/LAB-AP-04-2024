try:
    total_harga = int(input("Masukkan total harga yang harus dibayarkan: "))
    uang_diberikan = int(input("Masukkan jumlah uang yang diberikan oleh pelanggan: "))

    kembalian = uang_diberikan - total_harga
    
    print(f"Kembalian: Rp {kembalian}")

    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    rincian = {}
    for pecah in pecahan:
        if kembalian >= pecah:
            jumlah_lembar = kembalian // pecah
            kembalian -= jumlah_lembar * pecah
            rincian[pecah] = jumlah_lembar

    print("Rincian jumlah lembaran uang kembalian:")
    
    for pecah, jumlah in rincian.items():
        print(f"{jumlah} lembar Rp. {pecah}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
