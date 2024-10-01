try:
    n = int(input("masukkan tinggi pola: "))
except ValueError:
    print("Input tidak valid. Silahkan masukkan angka.")
    exit()
if n <= 1:
    print("Input tidak valid. Masukkan angka positif")
    exit()
for i in range (n+1) :
    if i % 2 != 1:
        continue
    bintang = " *" * i
    hasil = bintang.center(n * 3, " ")
    print(hasil)

for i in range(n - 1, -1, -1):
    if i % 2 == 0:  
        continue
    bintang = " *" * i
    hasil = bintang.center(n * 3, " ")
    print(hasil)

    



    