def hitung_langkah(n):
        langkah = 0
        if n % 2 == 0:
            n //= 2
            print(n)  # Cetak nilai pertama
        else:
            n = (n * 3) + 1
            print(n)  # Cetak nilai pertama
        langkah += 1
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = (n * 3) + 1
            print(n)
            langkah += 1
        print(f"Jumlah langkah: {langkah}")

# Input
try:
    n = float(input("Masukan angka: "))
    hitung_langkah(n)
    if n <= 0:
        print("Angka tidak boleh 0 dan dibawah 0")
except:
    print("Input tidak valid")