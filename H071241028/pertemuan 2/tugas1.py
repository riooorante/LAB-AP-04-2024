a = int(input("Masukkan panjang sisi 1: "))
b = int(input("Masukkan panjang sisi 2: "))
c = int(input("Masukkan panjang sisi 3: "))

if (a > c): 
    a, c = c, a
if (b > c):
    b, c = c , b
if (a > b):
    a, b = b, a

if a <= 0 or b <= 0 or c <= 0:
    print("Input tidak valid")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Tidak membentuk segitiga yang valid")

else:
    if ( a == b == c):
        jenisSegitiga = "Segitiga sama sisi"
    elif( a == b or b == c or a == c):
        jenisSegitiga = "Segitiga sama kaki"
    else:
        jenisSegitiga = " Segitiga sembarang"
    print("jenis segitiga: ", jenisSegitiga)
 
