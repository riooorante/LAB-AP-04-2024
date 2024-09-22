try:
    jumlah_baris = int(input("Masukkan jumlah baris: "))
except ValueError: 
    print("Input tidak valid")
    exit()

if jumlah_baris <= 0:
    print("Input tidak boleh nol atau kurang dari nol")
elif jumlah_baris <= 2:
    print("Tidak dapat membentuk belah ketupat")
else:
    if jumlah_baris % 2 == 1:                           #untuk jumlah baris ganjil
        for i in range(jumlah_baris):
            #bagian atas belah ketupat
            if i < jumlah_baris // 2:
                print('  ' * (jumlah_baris // 2 - i) + '* ' * (2 * i + 1))
            #bagian bawah belah ketupat
            else:
                print('  ' * (i - jumlah_baris // 2) + '* ' * (2 * (jumlah_baris - i - 1) + 1))

    else:                                               #untuk jumlah baris genap 
        for i in range(jumlah_baris):
            #bagian atas belah ketupat
            if i < jumlah_baris // 2:
                print('  ' * (jumlah_baris // 2 - i) + '* ' * (2 * i + 1))
            #bagian bawah belah ketupat
            else:
                print('  ' * ((i - jumlah_baris // 2) + 1) + '* ' * (2 * (jumlah_baris - i - 1) + 1))