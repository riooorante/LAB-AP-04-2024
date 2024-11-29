try:
    totalharga = int(input("Masukkann Total Harga: "))
    jumlahuang = int(input("Masukkann Jumlah Uang: "))

    kembalian = jumlahuang - totalharga

    if kembalian < 0:
        print("Uang yang diberikan tidak cukup.")
    elif kembalian == 0:
        print("Tidak ada kembalian.")
    else:
        print(f"Kembalian: {kembalian}")
        pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
        # Hitung jumlah lembar untuk setiap pecahan
        for uang in pecahan:
            jumlah_lembar = kembalian // uang
            kembalian %= uang
            if jumlah_lembar > 0:
                print(f"{jumlah_lembar} lembar Rp {uang:,}")
except ValueError:
    print("tidak valid")