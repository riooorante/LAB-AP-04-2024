import random
angka_rahasia = random.randint(1, 100)
percobaan = 0
maks_percobaan = 5

while percobaan < maks_percobaan:
    try: 
        tebakan = int(input("Masukkan tebakan anda (rules : angka lebih dari 0 dan tidak lebih dari 100)(0 untuk berhenti): "))
    except ValueError:
        print("Input tidak valid")
        percobaan+= 1
        continue
    
    if tebakan > angka_rahasia:
        print("Baca rules!")
        percobaan += 1
        continue

    if tebakan == 0:
        print("Kamu menghentikan permainan")
        break
    percobaan += 1

    if tebakan < 1:
        print("angka tidak valid")
        continue

    if tebakan == angka_rahasia:
        print("Selamat! anda menebak angka dengan benar.")
        break

    elif tebakan > angka_rahasia:
        print("Angka terlalu besar")

    else :
        print("Angka terlalu kecil")

if percobaan == maks_percobaan :
    print(f"Anda telah mencapai batas percobaan, jawabannya adalah {angka_rahasia}")