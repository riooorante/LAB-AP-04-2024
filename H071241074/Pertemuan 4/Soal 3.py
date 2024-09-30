def hitung_langkah(n):
    langkah = 0
    hasil = []

    while n != 1:
        hasil.append(float(n)) 

        
        if n % 2 == 0:
            n = n // 2

        else:
            n = (n * 3) + 1

        langkah += 1 

    hasil.append(float(1)) 
    return hasil, langkah


try:
    angka = int(input("Masukkan angka: ")) 

    if angka <= 0: 
        print("Input tidak valid")
    else:
        hasil, jumlah_langkah = hitung_langkah(angka)

        print("Urutan langkah:")
        for nilai in hasil:
            print(nilai)
        print(f"Jumlah langkah: {jumlah_langkah}")

except ValueError:  
    print("Input tidak valid")
