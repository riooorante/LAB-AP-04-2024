try: 
    jumlah_baris = int(input("Masukkan jumlah baris: "))
except ValueError:
    print("Input tidak valid")
    exit()

if jumlah_baris <= 0 :
    print("baris tidak boleh 0 atau dibawahnya")
elif jumlah_baris <=2 :
    print("Tidak bisa membentuk belah ketupat")
else :
    if jumlah_baris % 2 == 1:
        for i in range(jumlah_baris):
            if i < jumlah_baris // 2:
                print('  ' * (jumlah_baris // 2 - i) + '* ' * (2 * i + 1))
            else:
                print('  ' * (i - jumlah_baris // 2) + '* ' * (2 * (jumlah_baris - i - 1) + 1))

    else:
        for i in range(jumlah_baris):
            if i < jumlah_baris // 2:
                print('  ' * (jumlah_baris // 2 - i) + '* ' * (2 * i + 1))
            else:
                print('  ' * ((i - jumlah_baris // 2) + 1) + '* ' * (2 * (jumlah_baris - i - 1) + 1))
