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

    LYCKA TILL OCH SPELA ANSVARSFULLT!
    """)




player_money = 100000

time.sleep(1)

introduction()

def blackjack():

    while True:
        blackbet = float(input(f"Hur mycket vill du satsa?: "))
        if blackbet > player_money:
            print("Du får bara spela med pengar du har! ")
        else:
            break


    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [f"{value} of {suit}" for suit in suits for value in values]
        random.shuffle(deck)
        return deck

    def calculate_score(hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
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

    def blackjack():
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
                return
            elif player_score > 21:
                print("You bust! Dealer wins!")
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
            blackbet = blackbet*2
            player_money = player_money + blackbet
            print("Du har:")
            print(player_money)
        else:
            print("Dealer wins!")
            player_money = player_money - blackbet
            print("Du har:")
            print(player_money)

    # Huvudmeny
    while True:
        black = input("Tryck (s) för att starta Blackjack (q) för att gå tillbaka: ").lower()
        if black == "q":
            print("Avslutar spelet.")
            break
        elif black == "s":
            blackjack()
        else:
            print("Felaktig inmatning, försök igen.")



    
def slots():
    pass    

def roulette():
    pass

while True:
    startmeny = input(
    '''
    (1). Vill du gå till casinot?
    (2). Vill du gå hem och inte gambla?
    ''' 
    )
    if startmeny =="1":
        while True:
            huvudmeny = input(
            '''
    (1). Vill du spela slots?
    (2). Vill du spela Blackjack?
    (3). Vill du spela Roulette?
    (4). Vill du gå hem?
    (5). Vill du visa dina pengar
            '''
            )
            if huvudmeny =="1":
                slots()
            if huvudmeny =="2":
                blackjack()
            if huvudmeny =="3":
                roulette()
            if huvudmeny =="4":
                break
            if huvudmeny =="5":
                print(player_money)
    if startmeny =="2":
        break
    elif startmeny !="1" and startmeny !="2":
        print("Du måste välja mellan 1 eller 2")
