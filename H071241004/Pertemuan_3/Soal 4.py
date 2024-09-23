pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# total_harga = int(input("Masukkan total harga: "))
# uang_diberikan = int(input("Masukkan uang yang diberikan: "))

while True:
    total_harga_input = input("Masukkan total harga: ")
    if total_harga_input.isdigit():
        total_harga = int(total_harga_input)
        break
    else:
        print("Mohon masukkan angka untuk total harga.")

while True:
    uang_diberikan_input = input("Masukkan uang yang diberikan: ")
    if uang_diberikan_input.isdigit():
        uang_diberikan = int(uang_diberikan_input)
        break
    else:
        print("Mohon masukkan angka untuk uang yang diberikan.")

kembalian = uang_diberikan - total_harga

if kembalian < 0:
    print("Uang yang diberikan kurang!")
else:
    print("\nKembalian:")
    for nilai in pecahan:
        if kembalian >= nilai:
            jumlah = kembalian // nilai
            print(f"{jumlah} lembar Rp {nilai:,}")
            kembalian = kembalian % nilai