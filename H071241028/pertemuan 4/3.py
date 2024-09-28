def process_number(n):
    """Proses bilangan hingga mencapai 1 dan menghitung jumlah langkah."""
    steps = 0
    while n != 1:
        print(float(n))  # Tampilkan nilai n
        if n % 2 == 0:
            n = n / 2  # Jika genap
        else:
            n = n * 3 + 1  # Jika ganjil
        steps += 1
    print(float(n))  # Tampilkan 1
    return steps

def main():
    """Fungsi utama untuk menjalankan program."""
    try:
        n = int(input("Masukkan angka: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Input tidak valid")
        return

    steps = process_number(n)
    print(f"Jumlah langkah: {steps}")

# Memulai program
main()
