"""
20. nadogradite prethodni zadatak na nacin da ubacite u aparat i opciju za dodavanje mlijeka u kavu. kada korisnik ubaci kovanicu, aparat ga treba pitati zeli li kavu sa mlijekom ili bez. ukoliko korisnik odabere kavu sa mlijekom, ona se nasumicno uklanja iz sljedeceg seta: set_mlijeko = {1, 2, 3}. ukoliko korisnik zatrazi kavu sa mlijekom, a u aparatu ga vise nema, treba ispisati odgovarajucu poruku i po vasoj zelji nastaviti izvodjenje (npr. pitati korisnika za novu kavu ili mu isporuciti kavu bez mlijeka). u svim slucajevima treba se ispisati kakva je kava isporucena, koliko novca je ubaceno te koliki je iznos novca u aparatu nakon isporuke kave.
"""

from random import *

coffee_set = {1, 2, 3, 4, 5, 6}
milk_set  = {1, 2, 3}
collected_amount = 0

while True:
    x = input("Kovanica (ili q): ")
    if x.lower() == "q" or x == "0":
        break

    amount = int(x)
    chosen_set = coffee_set
    choice = input("kava sa mljekom ili bez (1, 2) ? ")
    if choice == "2":
        chosen_set = milk_set

    if len(chosen_set) == 0:
        print("Nema kave")
        continue

    if amount == 5:
        print(f"{'kava obična' if chosen_set == coffee_set else 'kava sa mljekom'}: {chosen_set.pop()}")
        print(f"{'kava obična' if chosen_set == coffee_set else 'kava sa mljekom'}: {chosen_set.pop()}")
        collected_amount += 5
    elif amount == 2:
        print(f"{'kava obična' if chosen_set == coffee_set else 'kava sa mljekom'}: {chosen_set.pop()}")
        collected_amount += 2

    if collected_amount >= 20:
        collected_amount = 0
        chosen_set.update([randint(1, 6) for _ in range(3)])
        