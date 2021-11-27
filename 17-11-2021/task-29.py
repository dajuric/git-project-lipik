"""
29. napravite program koji ce simulirati izvlacenje karti iz spila. program mora imati sljedece:
    - spil od 20 karti
    - 4 razlicite boje
    - 5 brojeva za svaku boju
program treba imati mogucnost povlacenja 3 karte, povlacenja 1 karte, mijesanja spila, zbrajanja bodova (brojevi na kartama).
kreirajte izbornik sa mogucnoscu izbora opcije (zapocni igru, zavrsi igru) -> ako korisnik odabere "zapocni igru", spil se mijesa te se povlace 3 karte. igraca se zatim pita hoce li povuci dodatnu kartu ili ne. ako odabere novu kartu, ona se dodaje u ruku; u suprotnom se broj bodova usporedjuje sa protivnikom. koristeci random varijablu (12-20), kreirajte protivnika, gdje random varijabla predstavlja njegov broj bodova. program treba racunati trenutni broj bodova te ako on prelazi 20, ispisati "izgubio si" i pitati korisnika zeli li ponovno igrati ili ne. ukoliko igrac pobijedi, treba ispisati poruku: pobijedio si i postaviti pitanje za novom igrom.
"""

import random

colors = ["herc", "karo", "pik", "tref"]
nums = ["1", "2", "3", "4", "5"]

def constructDeck():
    for c in colors:
        for n in nums:
            yield c + "-" + n

def shuffleDeck(deck: list):
    deck = list(deck)
    random.shuffle(deck)
    return deck

def takeCards(deck: list, n: int):
    cards = []
    for _ in range(n):
        r = random.randint(0, len(deck)-1)
        cards.append(deck[r])
        deck.remove(deck[r])

    return cards

def getPoints(cards: list):
    s = 0
    for c in cards:
        n = int(c.split("-")[1])
        s += n
    return s


playerCards = []
computerCards = []

while True:
    choice = input("Započni igru ? (d/n) ")
    if choice == "n":
        break

    deck = constructDeck()
    deck = shuffleDeck(deck)

    computerCards = takeCards(deck, 3)
    playerCards = takeCards(deck, 3)

    while True:
        oneCardChoice = input("Još jedna karta ? (d/n) ")
        if oneCardChoice == "d":
            playerCards += takeCards(deck, 1)
            computerCards += takeCards(deck, 1)
        else:
            cPoints = getPoints(computerCards)
            pPoints = getPoints(playerCards)
            print("Izgubio si" if cPoints > pPoints else "Pobjeda!")
            break
