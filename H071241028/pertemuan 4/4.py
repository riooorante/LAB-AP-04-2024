def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")

    while True:
        try:
            angka1 = float(input("Angka pertama: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    while True:
        try:
            angka2 = float(input("Angka kedua: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    
    while True:
        operasi = input("Operasi (+, -, *, /): ")
        if operasi in ['+', '-', '*', '/']:
            break
        else:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")

    if operasi == '+':
        hasil = angka1 + angka2
    elif operasi == '-':
        hasil = angka1 - angka2
    elif operasi == '*':
        hasil = angka1 * angka2
    elif operasi == '/':
        if angka2 == 0:
            return print("Pembagian dengan nol tidak diperbolehkan.")
        hasil = angka1 / angka2

    print(f"Hasil: {int(hasil)}")

kalkulator()
