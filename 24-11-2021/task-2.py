"""
2. Ponudi korisniku unos dok ne unese '!#quit$', svaku liniju zapisuj u datoteku.
"""

f = open("proba.txt", "w")

while True:
    x = input("Unos: ")
    if x == "q":
        break

    f.write(x + "\n")

f.close()