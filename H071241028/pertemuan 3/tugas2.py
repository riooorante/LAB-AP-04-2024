import random

secret_num = random.randint(1, 100)
maksimal_tebakan = 5

for i in range(maksimal_tebakan):
    try:
        tebakan = input("Masukkan tebakan Anda (0 untuk berhenti): ")

        if tebakan == '0':
            print("Permainan dihentikan. Terima kasih telah bermain!")
            break
        
        tebakan = int(tebakan)

        if tebakan < secret_num:
            print("Angka terlalu kecil.")
        elif tebakan > secret_num:
            print("Angka terlalu besar.")
        else:
            print("Selamat! Anda menebak angka dengan benar.")
            break  

    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

    if i+1 >= maksimal_tebakan:
        print(f"Anda telah menggunakan semua percobaan yang tidak valid. Angka rahasia adalah {secret_num}.")
