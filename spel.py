import time
import random

print("""  
     ████████████████████████████
      ███████ CASINO ████████████
    ██████████████████████████████
   ████████████████████████████████
  ██████████████████████████████████
 ████▀                           ▀████
██▀                                 ▀██
██                                   ██
██                                   ██
██          █████████████            ██
██         ███ SLOTS  ████           ██
██         ███████████████           ██
██                                   ██
██   ♠ ♦ ♥ ♣  BLACKJACK  ♣ ♥ ♦ ♠     ██
██       (Beat the dealer!)          ██
██                                   ██
██        🌀 ROULETTE 🎯            ██
██        (Spin & win!)              ██
██                                   ██
 ▀███████████████████████████████████▀
   ▀███████████████████████████████▀
      ▀█████████████████████████▀
         ▀███████████████████▀
            ▀█████████████▀
""")

def introduction():
    print("""
    VÄLKOMMEN TILL CASINO SPEL!
    
    REGLER:
    - Du börjar spelet med 100000 kronor i startkapital som du tog ut via sms lån.
    - Du kan spela följande spel:
        1. Slots
        2. Blackjack
        3. Roulette
    - I varje spel kan du satsa pengar:
        - Om du vinner, läggs din vinst till dina pengar.
        - Om du förlorar, dras din insats från dina pengar.
    - Om du får slut på pengar, måste du lämna casinot.

    ALLMÄN INFORMATION:
    - För att spela, välj ett spel från menyn.
    - Du kan när som helst lämna casinot och avsluta spelet.

    """)

player_money = 100000

time.sleep(1)

introduction()

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack(10)', 'Queen(10)', 'King(10)', 'Ace']
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'Jack(10)': 10, 'Queen(10)': 10, 'King(10)': 10, 'Ace': 11}
    score = 0
    aces = 0
    for card in hand:
        value = card.split(' ')[0]
        score += values[value]
        if value == 'Ace':
            aces += 1
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def display_hand(hand, owner):
    print(f"{owner}'s hand: {', '.join(hand)}")

def play_blackjack():
    global player_money
    while True:
        blackbet = float(input(f"Hur mycket vill du satsa?: "))
        if blackbet > player_money:
            print("Du får bara spela med pengar du har! ")
        else:
            break

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        display_hand(player_hand, "Player")
        print(f"Dealer's hand: {dealer_hand[0]}, Hidden")

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        if player_score == 21:
            print("Blackjack! You win!")
            player_money += blackbet * 2
            print(f"Du har: {player_money}")
            return
        elif player_score > 21:
            print("You bust! Dealer wins!")
            player_money -= blackbet
            print(f"Du har: {player_money}")
            return

        move = input("Do you want to (h)it or (s)tand? ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
        elif move == 's':
            break
        else:
            print("Invalid input. Please choose 'h' or 's'.")

    print("\nDealer's turn.")
    display_hand(dealer_hand, "Dealer")
    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)
        display_hand(dealer_hand, "Dealer")

    print("\nFinal results:")
    display_hand(player_hand, "Player")
    display_hand(dealer_hand, "Dealer")

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
        player_money += blackbet * 2
    else:
        print("Dealer wins!")
        player_money -= blackbet

    print(f"Du har: {player_money}")



def slots():
    leave ="a"
    while leave !="q":
        global player_money
        while True:
            slotsbet = float(input(f"Hur mycket vill du satsa?: "))
            if slotsbet > player_money:
                print("Du får bara spela med pengar du har! ")
            else:
                break

        symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
        
        reel1 = random.choice(symbols)
        reel2 = random.choice(symbols)
        reel3 = random.choice(symbols)

        print(f"{reel1} | {reel2} | {reel3}")

        if reel1 == reel2 == reel3:
            print("Jackpot!")
            player_money += slotsbet * 3
            print(f"Du har: {player_money}")
            leave = input("Tryck (q) ifall du vill lämna slots, Tryck (Enter) ifall du vill köra igen")
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            print("Grattis! Två hjul visar samma symbol!")
            player_money += slotsbet * 1.5
            print(f"Du har: {player_money}")
            leave = input("Tryck (q) ifall du vill lämna slots, Tryck (Enter) ifall du vill köra igen")
        elif reel1 == "7️⃣" and reel2 == "7️⃣" or reel1 == "7️⃣" and reel3 == "7️⃣" or reel2 == "7️⃣" and reel3 == "7️⃣":
            print("Grattis! Du fick två 7️⃣!")
            player_money += slotsbet * 2
            print(f"Du har: {player_money}")
            leave = input("Tryck (q) ifall du vill lämna slots, Tryck (Enter) ifall du vill köra igen")
        else:
            print("Tyvärr, ingen vinst. Försök igen!")
            player_money -= slotsbet
            print(f"Du har: {player_money}")
            leave = input("Tryck (q) ifall du vill lämna slots, Tryck (Enter) ifall du vill köra igen!")
        
def roulette():
        
    leave ="a"
    while leave !="q":
        global player_money
        while True:
            roulettebet = float(input(f"Hur mycket vill du satsa?: "))
            if roulettebet > player_money:
                print("Du får bara spela med pengar du har! ")
            else:
                break

    def spin_roulette():
        number = random.randint(0, 36)
        color = "red" if number % 2 == 0 else "black"
        if number == 0:
            color = "green"
        return number, color

    def main():
        print("Välkommen till Roulette!")
        print("Du kan satsa på:")
        print("1. Ett specifikt nummer (0-36)")
        print("2. Färg (red eller black)")
        print("3. Jämnt eller ojämnt (even eller odd)")

        while True:
            print("\nVad vill du satsa på?")
            print("1: Nummer")
            print("2: Färg")
            print("3: Jämnt/Ojämnt")
            print("4: Avsluta spelet")

            choice = input("Välj ett alternativ (1-4): ")

            if choice == "4":
                print("Tack för att du spelade!")
                break

            if choice == "1":
                bet_number = input("Välj ett nummer mellan 0 och 36: ")
                if not bet_number.isdigit() or not (0 <= int(bet_number) <= 36):
                    print("Ogiltigt nummer. Försök igen.")
                    continue
                bet_number = int(bet_number)
                result_number, result_color = spin_roulette()
                print(f"Roulette-resultat: {result_number} ({result_color})")
                if bet_number == result_number:
                    print("Grattis! Du gissade rätt nummer!")
                    player_money += roulettebet*36
                else:
                    print("Tyvärr, fel nummer.")
                    player_money -= roulettebet

            elif choice == "2":
                bet_color = input("Välj en färg (red eller black): ").lower()
                if bet_color not in ["red", "black"]:
                    print("Ogiltig färg. Försök igen.")
                    continue
                result_number, result_color = spin_roulette()
                print(f"Roulette-resultat: {result_number} ({result_color})")
                if bet_color == result_color:
                    print("Grattis! Du gissade rätt färg!")
                    player_money += roulettebet*2
                else:
                    print("Tyvärr, fel färg.")
                    player_money -= roulettebet

            elif choice == "3":
                bet_parity = input("Välj (even eller odd): ").lower()
                if bet_parity not in ["even", "odd"]:
                    print("Ogiltigt val. Försök igen.")
                    continue
                result_number, result_color = spin_roulette()
                print(f"Roulette-resultat: {result_number} ({result_color})")
                if result_number == 0:
                    print("Numret är 0, ingen vinst.")
                elif (result_number % 2 == 0 and bet_parity == "even") or (result_number % 2 != 0 and bet_parity == "odd"):
                    print("Grattis! Du gissade rätt!")
                    player_money += roulettebet*2
                else:
                    print("Tyvärr, fel val.")
                    player_money -= roulettebet

            else:
                print("Ogiltigt val. Försök igen.")

    if __name__ == "__main__":
        main()

    

    


while True:
    startmeny = input(
    '''
    (1). Vill du gå till casinot?
    (2). Vill du gå hem och inte gambla?
    '''
    )
    if startmeny == "1":
        while True:
            if player_money == 0:
                print("Du har inga pengar kvar att spela med. Gå hem och försök igen senare.")
                break
            huvudmeny = input(
            '''
    (1). Vill du spela slots?
    (2). Vill du spela Blackjack?
    (3). Vill du spela Roulette?
    (4). Vill du gå hem?
    (5). Vill du visa dina pengar
            '''
            )
            if huvudmeny == "1":
                slots()
            elif huvudmeny == "2":
                play_blackjack()  
            elif huvudmeny == "3":
                roulette()
            elif huvudmeny == "4":
                break
            elif huvudmeny == "5":
                print(f"Du har: {player_money} kronor")
    elif startmeny == "2":
        break
    else:
        print("Du måste välja mellan 1 eller 2")

print("Tack för att du spelade!")
