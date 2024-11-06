try :
    n = int(input("masukkan jumlah baris yang ingin ditampilkan = "))
    while n < 0 :
        n = int(input("Masukkan angka bukan dibwah 0 : "))
    for i in range(1,(n + 2)//2):
        print('  ' * (n-i) + '* ' * (2*i-1))
    for i in range(((n+1)//2),0,-1):
        print('  ' * (n-i) + '* ' * (2*i-1))
except:
    print("Anda memasukkan bukan angka")


