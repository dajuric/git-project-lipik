"""
4. Omogući unos, dok se ne unese '!#quit$'. Pitajte korisnika želi li unjeti knjigu.
Omogući popisivanje knjiga u skladištu.
Svaka knjiga ima naslov, autora, godinu izdanja, te cijenu. Nakon unosa svake knjige, upitajte korisnika
želi li unjeti još jednu knjigu. Svaku knjigu zapisati u datoteku.
"""

f = open("knjige.txt", "w")

while True:
    x = input("Naslov, autor, godina, cijena: ")
    if x == "q":
        break

    f.write(x + "\n")

f.close()