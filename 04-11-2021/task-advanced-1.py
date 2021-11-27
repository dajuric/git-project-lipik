"""
1. Neka program omoguci unos do trenutka kad je unesen broj -1. Korisnik unosi stringove, a program vraca slucajne recenice iz zbirke mogucih odgovora.
"""

answers = [
    "Ovo je prva rečenica",
    "Ovo je druga rečenica",
    "Ovo je treća rečenica",
]


from random import *

while True:
    str = input("Unos: ")
    if str == "-1":
        break

    randIdx = randint(0, len(answers) - 1)
    print(answers[randIdx])
