def kalkulator():
    while True:
        try :
            nomor1 = float(input("Masukkan angka pertama: "))
            nomor2 = float(input("Masukkan angka kedua: "))
            break
        except ValueError as r:
            print(f"Input tidak valid {r}")
    operasi = input("Masukkan operasi yang diinginkan (+, -, *, /): ")
    if operasi == '+':
        hasil = nomor1 + nomor2
        print(f"Hasil: {nomor1} + {nomor2} = {hasil}")
    elif operasi == '-':
        hasil = nomor1 - nomor2
        print(f"Hasil: {nomor1} - {nomor2} = {hasil}")
    elif operasi == '*':
        hasil = nomor1 * nomor2
        print(f"Hasil: {nomor1} * {nomor2} = {hasil}")
    elif operasi == '/':
        try:
            nomor2 != 0
            hasil = nomor1 / nomor2
            print(f"Hasil: {nomor1} / {nomor2} = {hasil}")            
        except ZeroDivisionError as a:
            print(f"Input Tidak Valid {a}")
    else:
        print("Operasi tidak valid. Silakan masukkan salah satu dari (+, -, *, /).")

kalkulator()