"""
26. vas omiljeni carobni aparat za kavu je podivljao. aparat treba ispitivati korisnika za kavu sve dok on ne unese "Q" ili 0. aparat prihvaca samo kovanice od 2kn ili 5kn. kada korisnik ubaci kovanicu od 5kn, aparat nausmicno izbacuje dvije kave. kada korisnik ubaci kovanicu od 2kn, aparat nasumicno izbaci jednu kavu. ako aparat sakupi 20kn, on se magicno napuni za 3 (nasumicne) kave. neka set sljedeceg oblika simbolizira pocetnu kolicinu kave u aparatu: dict_kava = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}. 
"""
from random import *

def getCoffee(coffee_dict: dict):
    randomKey = choice(list(coffee_dict.keys()))
    if coffee_dict[randomKey] > 0:
        coffee_dict[randomKey] -= 1
        print(f"Kava: {randomKey}")
    else:
        print(f"Nema kave: {randomKey}")

def fillCoffee(coffee_dict: dict):
    for _ in range(3):
        randomKey = choice(list(coffee_dict.keys()))
        coffee_dict[randomKey] += 1


coffee_set = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}
collected_amount = 0

while True:
    x = input("Upit: ")
    if x.lower() == "q" or x == "0":
        break

    x = int(x)
    if x == 5:
        getCoffee(coffee_set)
        getCoffee(coffee_set)
        collected_amount += 5
    elif x == 2:
        getCoffee(coffee_set)
        collected_amount += 2
    else:
        print("Neispravan unos.")
        continue

    if collected_amount >= 20:
        collected_amount = 0
        fillCoffee(coffee_set)
        