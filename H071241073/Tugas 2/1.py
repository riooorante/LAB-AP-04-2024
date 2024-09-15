a = float(input("Masukkan panjang sisi pertama: ")) #sisi a
b = float(input("Masukkan panjang sisi kedua: ")) #sisi b
c = float(input("Masukkan panjang sisi ketiga: ")) #sisi c

if a <= 0 or b <= 0 or c <= 0 :
    print("inputan tidak valid")
elif a + b <= c or a + c <= b or b + c <= a :
    print("Tidak dapat membentuk segitiga valid")
elif a == b == c :
    print("Segitiga sama sisi")
elif a == b or a == c or b == c :
    print("Segitiga sama kaki")
else :
    print("Segitiga sembarang")