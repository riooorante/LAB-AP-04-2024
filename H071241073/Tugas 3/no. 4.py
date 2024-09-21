# total_harga = int(input("Masukkan total harga: "))
# uang = int(input("Masukkan uang yang diberikan: "))
try: 
    total_harga = int(input("Masukkan total harga: "))
except ValueError:
    print("Input tidak valid")
    exit()

try: 
    uang = int(input("Masukkan uang: "))
except ValueError:
    print("Input tidak valid")
    exit()

uang_kasir = [ 100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uang - total_harga
for k in uang_kasir:
    lembar = kembalian // k
    if kembalian >= k:
        kembalian %= k
        print(f"{lembar} lembar Rp {k}")
    