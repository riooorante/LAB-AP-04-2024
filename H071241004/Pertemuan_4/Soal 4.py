print("Selamat datang di Kalkulator Sederhana !")

def kalkulator_sederhana(a, b, operasi):
    if operasi == '+':
        return a + b
    elif operasi == '-':
        return a - b
    elif operasi == '*':
        return a * b
    elif operasi == '/':
        if b == 0:
            return "Pembagian dengan 0 tidak diperbolehkan"
        else:
            return a / b
    
try:
    a = int(input("Angka pertama: "))
    b = int(input("Angka kedua: "))
    operasi = input("Operasi (+, -, *, /): ")
    hasil = kalkulator_sederhana(a, b, operasi)
    print("hasil: ",(hasil))
except ValueError as e:
    print(f"Input tidak valid: {e}")