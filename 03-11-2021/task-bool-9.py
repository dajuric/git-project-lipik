"""
9. • Unesite dva broja
   • Ispitati sljedeći logički izraz
   • a>0 and b<a
   • Ako je prethodni izraz ispravan
   • Ispisati TRUE u suprotnom FALSE
"""

a = int(input("Broj A:"))
b = int(input("Broj B:"))

cond = a > 0 and b < a
print("TRUE" if cond else "FALSE")