"""
23. koristenjem funkcija i naucenog, napisi program koji racuna iznos racuna u ovisnosti o transakcijama. dnevnik transakcija prikazi ovako (D: 100, W: 200), dok ukupan iznos na racunu prikazuje sa (T: 1000). ako korisnik unese T = 1000 te povuce iznos od 350 (W: 350), aplikacija treba ispisati azurirano stanje T: 650. ako nakon toga korisnik uplati iznos na racun, npr. 200 (D: 200), program treba uvecati iznos racuna i azurirati ga (T: 850). unosom stringa "quit", program prekida se izvodjenje programa.
"""

import re

total = 0
while True:
    x = input("T|W|D = amount: (or q)")
    if x == "q":
        break

    match = re.search("([T|W|D])\s*=\s*([0-9]+)", x)  
    if match == None:
        print("Nevaljani unos.")
        continue

    action = match[1]; amount = int(match[2])
    if action == "W":
        if amount > total:
            print("Preveliki iznos za podizanje.")
            continue
        total -= amount
    elif action == "D":
        total += amount
    elif action == "T":
        total = amount

    print("Ukupni iznos je: " + str(total))