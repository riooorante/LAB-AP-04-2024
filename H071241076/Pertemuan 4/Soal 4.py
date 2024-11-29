def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    
    try:
        angka_1 = float(input("Angka pertama: "))
        angka_2 = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return
    
    operasi = input("Operasi (+, -, *, /): ")
    
    if operasi == '+':
        hasil = angka_1 + angka_2
    elif operasi == '-':
        hasil = angka_1 - angka_2
    elif operasi == '*':
        hasil = angka_1 * angka_2
    elif operasi == '/':
        if angka_2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        hasil = angka_1 / angka_2
    else:
        print("Operasi tidak valid!")
        return
    
    print(f"Hasil: {hasil}")
kalkulator()