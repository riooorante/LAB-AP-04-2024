a = int(input("Masukkan panjang sisi pertama : "))
b = int(input("Masukkan panjang sisi kedua : "))
c = int(input("Masukkan panjang sisi ketiga : "))

if (a < 1) or (b < 1) or (c < 1):
    print("Inputan tidak valid")
elif (a+b>c) and (b+c>a) and (c+a>b):
    if (a==b==c):
        print("Segitiga Sama Sisi")
    elif (a==b) or (b==c) or (c==a):
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")