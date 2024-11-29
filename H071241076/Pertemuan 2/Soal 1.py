print("Input Panjang Sisi")
sisi_a = float(input("Masukkan panjang sisi pertama: "))
sisi_b = float(input("Masukkan panjang sisi kedua: "))
sisi_c = float(input("Masukkan panjang sisi ketiga: "))

if sisi_a <= 0 or sisi_b <=0 or sisi_c <=0:
    print("Sisi tidak valid")
elif sisi_a + sisi_b <= sisi_c or sisi_a + sisi_c <= sisi_b or sisi_b + sisi_c <= sisi_a:
    print("Tidak dapat membentuk segitiga yang valid")
elif sisi_a == sisi_b == sisi_c:
    print("Segitiga Sama Sisi")
elif sisi_a == sisi_b or sisi_b == sisi_c or sisi_c == sisi_a:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")