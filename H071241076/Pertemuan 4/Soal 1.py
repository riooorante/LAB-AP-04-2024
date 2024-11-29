import random

def ambil_kartu():
    kartu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
    return random.choice(kartu)

def hitung_total_kartu(kartu_pemain):
    total = 0
    for nilai in kartu_pemain:
        total += nilai
    return total


def pemain_ambil_kartu(kartu_pemain):

    while True:
        total_pemain = hitung_total_kartu(kartu_pemain)
        print(f"Kartu Anda sekarang adalah: {total_pemain}")
        
        ambil = input("Ingin mengambil kartu lagi? (y/n): ").lower()
        if ambil == 'y':
            kartu_pemain.append(ambil_kartu()) 
            total_pemain = hitung_total_kartu(kartu_pemain)
    
            if total_pemain > 21:
                print(f"Kartu Anda sekarang adalah: {total_pemain}")
                print("Anda kalah! Kartu melebihi 21.")
                return False
        else:
            break 
    return True


def dealer_ambil_kartu(kartu_dealer):
    
    total_dealer = hitung_total_kartu(kartu_dealer)

    while total_dealer < 17:
        kartu_baru = ambil_kartu()
        kartu_dealer.append(kartu_baru) 
        total_dealer = hitung_total_kartu(kartu_dealer)

        print(f"Kartu dealer sekarang adalah: {total_dealer}")
    
    return total_dealer

##################################################

print("Selamat datang di Blackjack!")

kartu_pemain = [ambil_kartu()]
kartu_dealer = [ambil_kartu()]

if pemain_ambil_kartu(kartu_pemain): 
    print(f"Kartu dealer adalah: {hitung_total_kartu(kartu_dealer)}")
    
    total_dealer = dealer_ambil_kartu(kartu_dealer)
    print(f"Kartu dealer akhir adalah: {total_dealer}")

    total_pemain = hitung_total_kartu(kartu_pemain)

    if total_dealer > 21:
        print("Anda menang! Dealer melebihi 21.")
    elif total_pemain > total_dealer:
        print("Anda menang!")
    elif total_pemain == total_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")