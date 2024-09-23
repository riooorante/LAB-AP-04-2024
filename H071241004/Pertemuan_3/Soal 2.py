import random
    
angka_rahasia = random.randint(1, 100)
    
print("Selamat datang di permainan Tebak Angka!")
    
for percobaan in range (1,6):
    print(f"\n Percobaan ke-{percobaan}")
    tebakan = input("Masukkan tebakan Anda (0 untuk berhenti): ")
        
    if tebakan == '0':
        print("Anda memilih untuk keluar. Terima kasih telah bermain!")
        break

    try:
        tebakan = int(tebakan)
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka.")
        continue
        

    if tebakan < 0:
        print("Angka tidak boleh di bawah 0.")
    elif tebakan > 100:
        print("Angka tidak boleh di atas 100.")
    elif tebakan == angka_rahasia:
        print("Selamat! Anda menebak angka dengan benar.")
    elif tebakan < angka_rahasia:
        print("Angka terlalu kecil.")
    else:
        print("Angka terlalu besar.")

    if percobaan == 5:
        print(f"Kesempatan Anda Habis, Angka rahasia adalah {angka_rahasia}")