def hitung_langkah(n):
    langkah = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)
        langkah += 1
    return langkah


try:
    n = int(input("Masukkan bilangan bulat positif: "))
    if n <= 0:
        print("Input tidak Valid")

    langkah = hitung_langkah(n)
    
    if n > 0:
        print(f"Jumlah langkah: {langkah}")

except ValueError:
    print("Masukkan sebuah angka!")


