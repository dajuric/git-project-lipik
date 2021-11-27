"""
15. Program treba korisniku omogućiti unos broja bodova od 1-100. Zatim program treba prema
bodovnoj skali za svaki broj bodova ispisati o kojoj se ocjeni radi. Bodovne pragove je
potrebno odrediti kao uvjete u elif uvjetovanju prema tablici
"""

x = int(input())
if x < 0 or x > 100:
    print("Nevaljan unos.")
    exit(1)

if x >= 0 and x < 50:
    print("nedovoljan")
elif x >= 50 and x < 70:
    print("dovoljan")
else:
    print("izvrstan")