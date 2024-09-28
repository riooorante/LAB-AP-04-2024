def kalkulator_sederhana():
    print("Selamat datang di Kalkulator Sederhana!")

    try:
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return
    
    operasi = input("Operasi (+, -, *, /): ")
    if operasi not in ['+', '-', '*', '/']:
        print("Operasi tidak valid. Gunakan +, -, *, atau /")
        return
    
    if operasi == '+':
        hasil = angka_pertama + angka_kedua
    elif operasi == '-':
        hasil = angka_pertama - angka_kedua
    elif operasi == '*':
        hasil = angka_pertama * angka_kedua
    elif operasi == '/':
        if angka_kedua == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        else:
            hasil = angka_pertama / angka_kedua

    print(f"Hasil: {hasil}")

kalkulator_sederhana()