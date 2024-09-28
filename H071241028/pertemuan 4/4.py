def calculator():
    """Fungsi untuk kalkulator sederhana."""
    print("Selamat datang di Kalkulator Sederhana!")
    
    # Menerima input angka pertama
    while True:
        try:
            num1 = float(input("Angka pertama: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    # Menerima input angka kedua
    while True:
        try:
            num2 = float(input("Angka kedua: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    # Menerima input operasi
    while True:
        operation = input("Operasi (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")

    # Melakukan operasi yang diinginkan
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        result = num1 / num2

    # Menampilkan hasil
    print(f"Hasil: {result}")

# Memulai kalkulator
calculator()
