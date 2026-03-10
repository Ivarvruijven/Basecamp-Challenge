from random import shuffle
from time import sleep
userbalance = 0
inzet = 0

def black_jack():
    global userbalance
    global inzet
    userbalance-=inzet
    hand = []
    computer = []
    soorten = ["♥️", "♠️", "♦️", "♣️"]
    waarden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas"]
    deck = []
    for soort in soorten:
        for waarde in waarden:
            deck.append((waarde, soort))




    # 3x shufflen zodat het echt random is
    shuffle(deck)
    shuffle(deck)
    shuffle(deck)
    

    # Berekent de waarde van 1 kaart
    def kaart_waarde(kaart):
        waarde, soort = kaart

        if waarde in ["Boer", "Vrouw", "Heer"]:
            return 10
        elif waarde == "Aas":
            return 11
        else:
            return int(waarde)

    # Gebruikt de waarde van alle kaarten en telt ze bij elkaar op, als het boven de 21 is en er zit een aas in de hand dan word het automatisch -10 gedaam
    def hand_waarde(hand):
        totaal = 0
        azen = 0

        for kaart in hand:
            waarde = kaart_waarde(kaart)
            totaal += waarde
            if kaart[0] == "Aas":
                azen += 1

        while totaal > 21 and azen > 0:
            totaal -= 10
            azen -= 1

        return totaal

    # Geeft om en om kaarten aan de user en de computer
    def deal():
        
        kaart = deck.pop()
        hand.append(kaart)
        print(f"User: {hand}") 
        sleep(1)

        kaart_open = deck.pop()
        computer.append(kaart_open)
        print(f"Computer: {computer}")
        sleep(1)

        kaart = deck.pop()
        hand.append(kaart)
        print(f"User: {hand}") 
        sleep(1)
        
        kaart_gesloten = deck.pop()
        computer.append(kaart_gesloten)
        print(f"Computer: [{kaart_open}, (VERBORGEN)]")
        sleep(1)
        
        
        print(f"Waarde user: {hand_waarde(hand)}")
        sleep(1)
        print(f"Waarde computer open kaart: {kaart_waarde(kaart_open)}")
        sleep(1)
        print()
    deal()


    computer_blackjack = hand_waarde(computer) == 21 and hand_waarde(hand) != 21
    if computer_blackjack:
        print("Computer Blackjack!")
    if computer_blackjack != True:
        if hand_waarde(hand) < 21:
            keuze = input("Maak je keuze (nummer):\n1. Hit\n2. Stand\n")
            while keuze != "1" and keuze != "2":
                     keuze = input("Maak je keuze (nummer):\n1. Hit\n2. Stand\n")
            while keuze == "1":
                if keuze == "1":
                    kaart = deck.pop()
                    hand.append(kaart)
                    print()
                    print(f"User: {hand}")
                    print(f"Waarde user: {hand_waarde(hand)}")
                    print()
                    if hand_waarde(hand) > 21:
                        print("Bust!")
                        break
                    keuze = input("Maak je keuze (nummer):\n1. Hit\n2. Stand\n")
            if keuze == "2":
                print("Computer kaarten worden nu gedeeld")
                sleep(0.5)
                print("...")
                sleep(0.5)

    elif hand_waarde(hand) == 21:
        print("Blackjack!")
    print(f"Computer: {computer}")
    if hand_waarde(hand) < 21:
        while hand_waarde(computer) < 17:
            if hand_waarde(computer) < 21:
                kaart = deck.pop()
                computer.append(kaart)
                print()
                print(f"Computer: {computer}")
                sleep(1)
                print(f"Waarde computer: {hand_waarde(computer)}")
                sleep(1)
                print()
    if hand_waarde(computer) == hand_waarde(hand) and hand_waarde(hand) != 21:
        print()
        print("Push!")
        print(f"+€{inzet}")
        print(f"Waarde user: {hand_waarde(hand)}")
        print(f"Waarde computer: {hand_waarde(computer)}")
        userbalance+=inzet
    elif hand_waarde(hand) == 21 and len(hand) == 2 and hand_waarde(computer) != 21:
        print()
        print("User Blackjack!")
        print(f"+€{inzet*2.5}")
        userbalance+=(inzet*2.5)
    elif hand_waarde(computer) == 21 and len(computer) == 2 and hand_waarde(hand) == 21 and len(hand) == 2:
        print()
        print("Beide Blackjack, Push!")
        print(f"+€{inzet}")
        print(f"Waarde user: {hand_waarde(hand)}")
        print(f"Waarde computer: {hand_waarde(computer)}")
        userbalance+=inzet
    elif hand_waarde(computer) > 21 and hand_waarde(hand) <= 21:
        print()
        print("Computer bust, User wint!")
        print(f"+€{inzet}")
        waarde()
        userbalance+=(inzet*2)
    elif hand_waarde(computer) > hand_waarde(hand) and hand_waarde(computer) <= 21:
        print()
        print("Computer wint!")
        print(f"-€{inzet}")
        waarde()
    elif hand_waarde(hand) > 21 and hand_waarde(computer) <= 21:
        print()
        print("Computer wint!")
        print(f"-€{inzet}")
        waarde()    
    elif hand_waarde(computer) < hand_waarde(hand) and hand_waarde(hand) <= 21:
        print()
        print("User wint!")
        print(f"+€{inzet}")
        Waarde()
        userbalance+=(inzet*2)

def Waarde():
    print(f"Waarde user: {hand_waarde(hand)}")
    print(f"Waarde computer: {hand_waarde(computer)}")  

def keuzemenu ():
    global inzet
    global userbalance
    scorebalk()
    #gaat het keuzemenu weergeven, en slaat de keuze op. als waarde niet geldig is wordt er een error weergeven
    try:
        userkeuzemenu = int(input(f'VUL IN (getal):\n1:    starten\n2:    opwaarderen\n3:    inzet aanpassen\n4:    stoppen\n----------------------------\n'))
    except ValueError:
        print("dit is geen geldige invoer!")
        keuzemenu()
    #spel starten maar alleen als de inzet niet hoger is dan balence of inzet kleiner dan 0 is
    if userkeuzemenu == (1):
        # naar een def functie
        if userbalance < inzet or inzet <= 0:
            print("zorg dat je je inleg verlaagt, of je Balance opwaardeert!")
            keuzemenu()
        else:
            print("start het spel!")
            sleep(1)
            black_jack()
            keuzemenu()
    elif userkeuzemenu == (2): #opwaarderen
        try:
            userbalance = userbalance + int(input("met hoeveel euro wil je je account opwaarderen?\n€"))
        except ValueError:
            print("dit is geen geldige invoer!")
            keuzemenu()
        print (f'oke je nieuwe Balance is: €{userbalance} euro')
        keuzemenu()
    elif userkeuzemenu == (3): # inzet aanpassen
        try:
            inzet = int(input("hoeveel wordt je inzet:\n€"))
        except ValueError:
            print("dit is geen geldige invoer!")
            keuzemenu()
        keuzemenu()

    elif userkeuzemenu == (4): #stoppen spel
        print ("Dank voor het spelen")
        exit()
    else:
        print("dit is geen geldige invoer!")
        keuzemenu()
# de scorebalk met balance en inzet
def scorebalk():
    global inzet
    global userbalance
    print(f"----------------------------\nBALANCE: €{userbalance}  INZET: €{inzet}\n----------------------------")

keuzemenu()

