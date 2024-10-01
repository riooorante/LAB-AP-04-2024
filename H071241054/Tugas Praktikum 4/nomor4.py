def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    return a // b

print("Selamat datang di Kalkulator Sederhana!")

try:
    a = float(input("Angka pertama: "))
    b = float(input("Angka kedua: "))
    operasi = str(input("Operasi +, -, *, /: "))

    if operasi == "+":
        print(tambah(a, b))
    elif operasi == "-":
        print(kurang(a, b))
    elif operasi == "*":
        print(kali(a, b))
    elif operasi == "/":
        if b == 0:
            print("Pembagian dengan nol tidak diperbolehkan!")
        else:
            print(bagi(a, b))
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /.")

except ValueError as e:
    print(f"Input tidak valid: {e}")