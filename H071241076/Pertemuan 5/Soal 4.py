s = input("Masukkan string: ")

print("Semua substring yang mungkin:")
for panjang in range(1, len(s) + 1):

    for posisi_awal in range(len(s) - panjang + 1):

        substring = s[posisi_awal:posisi_awal + panjang]

        print(substring)