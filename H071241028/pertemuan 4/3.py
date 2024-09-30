def proses_bilangan(n):
    """Proses bilangan hingga mencapai 1 dan menghitung jumlah langkah."""
    langkah = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        print(float(n))  
        langkah += 1
    return langkah

try:
    n = int(input("Masukkan angka: "))
    if n <= 0:
        raise ValueError
except ValueError:
    print("Input tidak valid")
else:
    langkah = proses_bilangan(n)
    print(f"Jumlah langkah: {langkah}")
