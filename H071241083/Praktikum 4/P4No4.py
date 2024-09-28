def hitung(angka1, angka2, operasi):
    if operasi == '+':
        hasil = angka1 + angka2
        print(f"Hasil: {hasil}")
    elif operasi == '-':
        hasil = angka1 - angka2
        print(f"Hasil: {hasil}")
    elif operasi == '*':
        hasil = angka1 * angka2
        print(f"Hasil: {hasil}")
    elif operasi == '/':
        if angka2 == 0:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {hasil}")
    else:
        print("Operasi tidak valid. Harap pilih nomor operasi yang benar.")
        
        
print("Selamat datang di Kalkulator Sederhana")

try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    operasi = input("Operasi (+, -, *, /): ")
    
    hitung(angka1, angka2, operasi)

except ValueError:
    print("Input tidak valid. Harap masukkan sebuah angka.")


