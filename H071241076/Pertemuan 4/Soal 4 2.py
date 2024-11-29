# Operasi Matematika
def tambah(angka_1, angka_2):
    return angka_1 + angka_2

def kurang(angka_1, angka_2):
    return angka_1 - angka_2

def kali(angka_1, angka_2):
    return angka_1 * angka_2

def bagi(angka_1, angka_2):
    if angka_2 == 0:
        print("Pembagian dengan nol tidak diperbolehkan.")
        return None
    return angka_1 / angka_2

print("Selamat datang di Kalkulator Sederhana!")

try:
    angka_1 = float(input("Angka pertama: "))
    angka_2 = float(input("Angka kedua: "))
except ValueError as e:
    print(f"Input tidak valid: {e}")
else:
    operasi = input("Operasi (+, -, *, /): ")

    if operasi == '+':
        hasil = tambah(angka_1, angka_2)
    elif operasi == '-':
        hasil = kurang(angka_1, angka_2)
    elif operasi == '*':
        hasil = kali(angka_1, angka_2)
    elif operasi == '/':
        hasil = bagi(angka_1, angka_2)
        if hasil is None:
            hasil = "Tidak ada hasil karena pembagian dengan nol."
    else:
        hasil = "Operasi tidak valid!"
    
    print(f"Hasil: {hasil}")