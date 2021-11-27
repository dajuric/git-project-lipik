"""
27. nadogradite prethodni zadatak na nacin da ubacite u aparat i opciju za dodavanje mlijeka, secera ili meda u kavu. kada korisnik ubaci kovanicu, aparat ga treba pitati zeli li kavu sa dodatkom ili ne. postavite vrijednost svakog dodatka na 5, koristeci fromkeys. ukoliko korisnik zatrazi kavu sa sladilom kojega vise nema u aparatu, treba ispisati odgovarajucu poruku te ponuditi korisniku opciju bez dodatka ili povrat novca, nakon cega zavrsava sa izvodjenjem. u svim slucajevima treba se ispisati kakva je kava isporucena, sa kojim sladilom, koliko novca je ubaceno te koliki je iznos novca u aparatu nakon isporuke kave.
"""

from random import *

def getCoffee(coffee_dict: dict):
    randomKey = choice(list(coffee_dict.keys()))
    if coffee_dict[randomKey] > 0:
        coffee_dict[randomKey] -= 1
        print(f"Kava: {randomKey}")
    else:
        print(f"Nema kave: {randomKey}")


coffee_set = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}
add_set    = {}.fromkeys(["mljeko", "šećer", "med"], 5)
collected_amount = 0

while True:
    amount = input("Kovanica: ")
    if amount.lower() == "q" or amount == "0":
        break

    amount = int(amount)
    randomCoffee = choice(list(coffee_set.keys()))
    if coffee_set[randomCoffee] == 0:
        print(f"Nema kave: {randomCoffee}. Novac refundiran.")
        break

    randomAdd   = choice(list(add_set.keys()))
    if add_set[randomAdd] == 0:
        print(f"Nema dodatka: {randomAdd}.")
        choice = input("Nastaviti bez dodatak (d/n) ? ")
        if choice == "n":
            print("Ništa od kave.. Novac refundiran.")
            break
    else:
        add_set[randomAdd] -= 1
        print(f"Odabran dodatak {randomAdd}. ", end= " ")

    coffee_set[randomCoffee] -= 1
    print(f"Odabrana kava: {randomCoffee}.")

    collected_amount += amount
    print(f"--- Ubačeno je: {amount} novca. Ukupno novca u automatu je: {collected_amount}. ---")
