colors = ["herc", "karo", "pik", "tref"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "decko", "dama", "kralj"]

def constructDeck():
    for c in colors:
        for n in nums:
            yield c + "-" + n

import random

def shuffleDeck(deck):
    deck = list(deck)
    random.shuffle(deck)
    return deck

def takeCard(deck, index):
    return deck[index]

def distributeCards(deck, M, pCount):
    if M > len(deck):
        print("M je veći nego broj karata.")
        return []

    deck = list(deck)
    cardsPerPlayer = []
    for p in range(pCount):
        cardsPerPlayer.append([])
        for i in range(M):
            cardsPerPlayer[p].append(deck.pop())

    #print
    for i, cdp in enumerate(cardsPerPlayer):
        print(f"Karte za igrača {i}: {cdp}")
    print("Preostalo: " + str(deck))

    return cardsPerPlayer, deck


deck = constructDeck()
deck = shuffleDeck(deck)
distributeCards(deck, 10, 5)