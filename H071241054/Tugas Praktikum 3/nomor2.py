import random

angka_rahasia = random.randint(1, 101)
maksimal_percobaan = 5

for percobaan in range(1, maksimal_percobaan+1):
    try:
        tebakan = int(input(f"Percobaan {percobaan}: Masukkan tebakan Anda (ketik 0 untuk keluar): ")) 
        if tebakan == 0:
            print("Permainan dihentikan. Terima kasih telah bermain!")
            break
        elif tebakan <= 0:
            print("Tebakan harus di antara angka 1 - 100")
        else:
            if tebakan < angka_rahasia:
                print("Angka terlalu kecil.")
            elif tebakan > angka_rahasia:
                print("Angka terlalu besar.")
            else:
                print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar!")
                break

    except ValueError: 
        print("Input tidak valid. Harap masukkan angka")

else:
    print(f"Maaf, Anda telah menggunakan semua percobaan. Angka yang benar adalah {angka_rahasia}.")