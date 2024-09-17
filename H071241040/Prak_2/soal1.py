#Soal 1
a = float(input("Masukkan panjang sisi pertama : "))
b = float(input("Masukkan panjang sisi kedua : "))
c = float(input("Masukkan panjang sisi ketiga : "))
if a <= 0 or b <= 0 or c <= 0:
    print("Inputan tidak valid")
elif a == b ==c  :
    print("Segitiga sama sisi")
elif a == b or c==b or a==c:
    print("Segitiga sama kaki")
elif a != b and b != c and a!=c:
    print("Tidak dapat membentuk segitiga yang valid") if a+b >= c or a+c >=b or b+c>=a else print("Segitiga sembarang")
