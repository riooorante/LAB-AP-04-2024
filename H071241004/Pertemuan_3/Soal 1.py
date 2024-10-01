try:
    n = int(input("Masukkan Jumlah Baris: "))
except ValueError:
    print("Input tidak valid")
    exit()
spasi = "  "
genap = n % 2 == 0
ganjil = n % 2 != 0

if n <= 0:
    print("Jumlah baris tidak boleh 0 atau dibawah 0 ")
elif n <= 2:
    print("Jumlah baris tidak boleh 1 atau 2")
else:
    if genap:
        for i in range(1, n // 2 + 1):
            print((n - i) * spasi + (2 * i - 1) * '* ')
        for i in range(n // 2, 0, -1):
            print((n - i) * spasi + (2 * i - 1) * '* ')
    elif ganjil:
        for i in range(1, n // 2 + 2):
            print((n - i) * spasi + (2 * i - 1) * '* ')
        for i in range(n // 2, 0, -1):
            print((n - i) * spasi + (2 * i - 1) * '* ')
    else:
        print("Inputan yang dimasukkan tidak valid")   