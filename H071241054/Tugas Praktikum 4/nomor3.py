def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:          #jika n genap
            n = n/2
        else:                   #jika n ganjil
            n = n * 3 + 1
 
        langkah = langkah + 1
        print(n)
    return langkah

try:
    n = int(input("Masukkan bilangan bulat positif: "))
    if n <= 0:
        print("Input tidak Valid")

except ValueError:
    print("Input tidak Valid")

langkah = hitung_langkah(n)
print(f"Jumlah langkah: {langkah}")