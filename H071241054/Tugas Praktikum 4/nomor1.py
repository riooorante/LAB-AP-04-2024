import random

def total_skor(kartu):
    skor = sum(kartu)
    if 11 in kartu and skor > 21:
        skor = skor - 10
    return skor

def penentuan(skor_dealer, skor_pemain):
    if skor_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif skor_pemain > skor_dealer:
        print("Anda menang!")
    elif skor_pemain < skor_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

#memainkan permainan blackjack
print("Welcome to Blackjack!")
kartu_pemain = [random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])]       
kartu_dealer = [random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])]

skor_pemain = total_skor(kartu_pemain)
skor_dealer = total_skor(kartu_dealer)

print(f"Kartu anda sekarang adalah: {skor_pemain}")

while True:
    pilihan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
    if pilihan == 'y':
        kartu_pemain.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]))
        skor_pemain = total_skor(kartu_pemain)
        print(f"Kartu anda sekarang adalah: {skor_pemain}")
        if skor_pemain > 21:
            print("Anda kalah, kartu anda melebihi 21.")
            exit()
    else:
        if pilihan == 'n':
            break
        else:
            print("Input tidak valid. Masukkan (y/n) untuk memilih kartu!")

print(f"Kartu dealer adalah: {skor_dealer}")

while skor_dealer < 17:
    kartu_dealer.append(random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]))
    skor_dealer = total_skor(kartu_dealer)
    print(f"Kartu dealer sekarang adalah: {skor_dealer}")

penentuan(skor_dealer, skor_pemain)