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

def blackjack():
    pass

def slots():
    pass

def roulette():
    pass

while True:
    startmeny = input(
    '''
    1. Vill du gå till casinot?
    2. Vill du gå hem och inte gambla?
    ''' 
    )
    if startmeny =="1":
        while True:
            huvudmeny = input(
            '''
            1. Vill du spela slots?
            2. Vill du spela Blackjack?
            3. Vill du spela Roulette?
            4. Vill du gå hem?
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
    if startmeny =="2":
        break
    elif startmeny !="1" and startmeny !="2":
        print("Du måste välja mellan 1 eller 2")
