import random as r
print("============= Welcome to Blackjack! =============")
def kartu_acak():
    return r.randint(1, 11)

def player():
    total = kartu_acak()
    print("Kartu anda sekarang adalah:", total)
    while total <= 21:
        pilih = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if pilih == "y":
            total += kartu_acak()
            print("Kartu anda sekarang adalah:", total)
            if total > 21:
                print("Anda kalah!")
                break
        elif pilih == "n":
            break
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")
    return total
def dealer() :
    total = kartu_acak()
    print("Kartu dealer adalah:", total)
    while total < 17:
        total += kartu_acak()
        print("Kartu dealer sekarang adalah:", total)
    return total

def pemenang(player, dealer):
    if player > 21:
        print("Anda kalah, kartu anda melebihi 21.")
    elif dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player == dealer:
        print("Seri!")
    elif player > dealer:
        print("Anda menang!")
    else:
        print("Dealer menang!")
pemenang(player(), dealer())
