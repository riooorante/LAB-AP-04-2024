# import random

# def hit(kartu):
#     """Menarik kartu dari dek."""
#     return kartu.pop()

# def calculate_hand_value(hand):
#     """Menghitung nilai total kartu di tangan."""
#     value = sum(10 if card in ['J', 'Q', 'K'] else 11 if card == 'A' else int(card) for card in hand)
#     while value > 21 and 'A' in hand:
#         value -= 10
#     return value

# print("Welcome to Blackjack!")

# kartu = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A'] * 4
# random.shuffle(kartu)

# player_hand = [hit(kartu)]
# dealer_hand = [hit(kartu)]

# print(f"kartu anda sekarang adalah: {player_hand[0]}")

# while True:
#     pilihan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
#     if pilihan == 'y':
#         player_hand.append(hit(kartu))
#         print(f"kartu anda sekarang adalah: {calculate_hand_value(player_hand)}")
#         if calculate_hand_value(player_hand) > 21:
#             print("Anda kalah!")
#             break
#     elif pilihan == 'n':
#         break
#     else:
#         print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")

# if calculate_hand_value(player_hand) <= 21:
#     print(f"kartu dealer adalah: {dealer_hand[0]}")
#     while calculate_hand_value(dealer_hand) < 17:
#         dealer_hand.append(hit(kartu))
#     print(f"kartu dealer sekarang adalah: {calculate_hand_value(dealer_hand)}")

#     player_value = calculate_hand_value(player_hand)
#     dealer_value = calculate_hand_value(dealer_hand)

#     if dealer_value > 21:
#         print("Anda menang, dealer melebihi 21.")
#     elif player_value > dealer_value:
#         print("Anda menang!")
#     elif player_value < dealer_value:
#         print("Dealer menang!")
#     else:
#         print("Seri!")

def penjumlahan(*a,  b):
    print(a)
    hasil = sum(a,b)
    print(hasil)

penjumlahan(1,3, 1,2,4,5,4,3,2,4,6,7,5, b=7)