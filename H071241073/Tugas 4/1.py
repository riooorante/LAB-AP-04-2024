import random

def ambil_kartu():
    return random.randint(1, 11)

def hitung_total(kartu):
    total = sum(kartu)
    if total > 21 and 11 in kartu:
        kartu.remove(11)
        kartu.append(1)
        total = sum(kartu)
    return total

def blackjack():
    print("Welcome to Blackjack!")

    kartu_pemain = [ambil_kartu()]
    kartu_dealer = [ambil_kartu()]
    
    print(f"Kartu anda sekarang adalah: {kartu_pemain[0]}")

    while True:
        ambil_lagi = input("Apakah masih akan mengambil kartu? (y/n):\n").lower()
        if ambil_lagi == 'y':
            kartu_pemain.append(ambil_kartu())
            total_kartu_pemain = hitung_total(kartu_pemain)
            print(f"Kartu anda sekarang adalah: {total_kartu_pemain}")
            if total_kartu_pemain > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif ambil_lagi == 'n':
            break
        else:
            print("Input tidak valid, coba lagi.")
    
    print(f"Kartu dealer adalah: {kartu_dealer[0]}")
    while hitung_total(kartu_dealer) < 17:
        kartu_dealer.append(ambil_kartu())
        print(f"Kartu dealer sekarang adalah: {hitung_total(kartu_dealer)}")
    
    total_kartu_pemain = hitung_total(kartu_pemain)
    total_dealer = hitung_total(kartu_dealer)

    hasil(total_kartu_pemain, total_dealer)

def hasil(total_kartu_pemain, total_dealer):
    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_kartu_pemain > total_dealer:
        print("Anda menang!")
    elif total_kartu_pemain == total_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack()