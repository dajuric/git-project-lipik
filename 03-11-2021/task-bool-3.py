"""
3. Unesite dva broja. Zbrojite dva broja. Ako je zbroj veći od 20 ispišite : Suma je veća od 20 u
suprotnom ispišite: Suma je manja od 20
"""

x = int(input())
y = int(input())

a = x + y
if a > 20:
    print("Suma je veća od 20")
else:
    print("Suma je manja od 20 (ili jednaka).")