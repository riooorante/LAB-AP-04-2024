import random

angka_rahasia = random.randint(1,100)

print("Selamat datang di permainan tebak angka!")
print("Saya telah memilih angka antara 1 hingga 100.")
print("Anda memiliki maksimal 5 kali percobaan untuk menebak angka.")
print("Ketik '0' untuk keluar dari permainan.")
kesempatan = 0
while True:
    print(f"\n Percobaan ke-{kesempatan}")
    print(angka_rahasia)
    
    kesempatan += 1
    
    try:
        tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti) : "))
        if tebakan == 0:
            print("Anda telah keluar dari permainan.")
            break
        elif tebakan < 0:
            print("Angka tidak boleh dibawah 0")
        elif tebakan > 100:
            print("Angka tidak boleh diatas 100")
        elif tebakan == angka_rahasia:
            print(f"Selamat! Anda berhasil menebak angka yang benar adalah {angka_rahasia}.")
            break
        elif tebakan < angka_rahasia:
            print("Angka terlalu kecil.")
        else:
            print("Angka terlalu besar.")
    except:
        print("Harap memasukkan sebuah angka")