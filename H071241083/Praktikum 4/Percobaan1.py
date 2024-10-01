import random

def draw_card():
    """Mengambil kartu secara acak dari dek."""
    return random.randint(1, 11)  # Kartu antara 1 dan 11

def calculate_total(cards):
    """Menghitung total nilai kartu."""
    return sum(cards)

def player_turn():
    """Menjalankan giliran pemain."""
    player_cards = [draw_card()]
    
    while True:
        print(f"Kartu anda sekarang adalah: {calculate_total(player_cards)}")
        action = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if action == 'y':
            player_cards.append(draw_card())
            if calculate_total(player_cards) > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return None
        elif action == 'n':
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 'n'.")
    return player_cards

def dealer_turn():
    """Menjalankan giliran dealer."""
    dealer_cards = [draw_card()]
    print(f"Kartu dealer adalah: {calculate_total(dealer_cards)}")
    while calculate_total(dealer_cards) < 17:
        dealer_cards.append(draw_card())
        print(f"Kartu dealer sekarang adalah: {dealer_cards}, total: {calculate_total(dealer_cards)}")
    return dealer_cards

def determine_winner(player_total, dealer_total):
    """Menentukan pemenang dari permainan."""
    if player_total > 21:
        return "Anda kalah!"
    elif dealer_total > 21:
        return "Anda menang, dealer melebihi 21!"
    elif player_total > dealer_total:
        return "Anda menang!"
    elif player_total < dealer_total:
        return "Dealer menang!"
    else:
        return "Seri!"

def play_blackjack():
    """Fungsi utama untuk menjalankan permainan Blackjack."""
    print("Welcome to Blackjack!")
    
    player_cards = player_turn()
    if player_cards is None :  # Jika pemain sudah kalah
        return

    dealer_cards = dealer_turn()
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)

    print(determine_winner(player_total, dealer_total))

play_blackjack()
