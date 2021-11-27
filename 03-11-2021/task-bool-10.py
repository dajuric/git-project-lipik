"""
10. • Unesite dva broja
    • Ispitati sljedeći logički izraz
    • a>0 and b<a
    • Ako je prethodni izraz ispravan
    • Ispisati TRUE te provjeriti sljedeći
    • logički izraz a>b or b>0
    • u suprotnom ispisati FALSE
    • Ako je prethodni izraz ispravan
    • Ispisati TRUE
    • u suprotnom FALSE
"""

a = int(input("Broj A:"))
b = int(input("Broj B:"))

if a > 0 and b < a:
    print("TRUE")

    if a > b and b > 0:
        print("TRUE")
    else:
        print("FALSE")
else:
    print("FALSE")