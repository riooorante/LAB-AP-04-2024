import random

angka_rahasia = random.randint(1, 100)
percobaan = 0
maksimal_percobaan = 5

print("Tebak angka antara 1 dan 100. Masukkan '0' untuk berhenti.")

# Mulai permainan
while percobaan < maksimal_percobaan:
    try:
        tebakan = int(input("Masukkan tebakan Anda: "))

        if tebakan == 0:
            print("Permainan dihentikan.")
            break

        percobaan += 1

        if tebakan == angka_rahasia:
            print("Selamat! Anda menebak dengan benar.")
            break
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar.")
        else:
            print("Angka terlalu kecil.")

    except ValueError:
        percobaan += 1
        print("Input tidak valid. Masukkan angka antara 1 dan 100.")
if percobaan == maksimal_percobaan:
    print(f"Maaf, kesempatan habis. Angka yang benar adalah {angka_rahasia}.")
