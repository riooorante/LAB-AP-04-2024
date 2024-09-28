import random

def total_skor(kartu):
    skor = sum(kartu)
    if 11 in kartu and skor > 21:
        skor = skor - 10
    return skor

def draw_card():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])  #1 & 11 mewakili As, dan 10 mewakili J, K, Q

def play_blackjack():
    print("Welcome to Blackjack!")
    
    kartu_pemain = [draw_card()]
    kartu_dealer = [draw_card()]
    
    skor_pemain = total_skor(kartu_pemain)
    skor_dealer = total_skor(kartu_dealer)
    
    print(f"Kartu anda sekarang adalah: {skor_pemain}")

    #pemain mengambil kartu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    while True:
        pilihan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if pilihan == 'y':
            kartu_pemain.append(draw_card())
            skor_pemain = total_skor(kartu_pemain)
            print(f"Kartu anda sekarang adalah: {skor_pemain}")
            if skor_pemain > 21:
                print("Anda kalah, kartu anda melebihi 21.")
        elif pilihan == 'n':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

    print(f"Kartu dealer adalah: {skor_dealer}")
    
    #dealer mengambil kartu hingga mencapai 17 atau lebih
    while skor_dealer < 17:
        kartu_dealer.append(draw_card())
        skor_dealer = total_skor(kartu_dealer)
        print(f"Kartu dealer sekarang adalah: {skor_dealer}")

    #menentukan hasil permainan
    if skor_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif skor_pemain > skor_dealer:
        print("Anda menang!")
    elif skor_pemain < skor_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

play_blackjack()