"""
4. • Unesite dva broja. Pomnožite ih i zbrojite. Ispišite umnožak i zbroj.
   • Provjerite da li su zbroj i umnožak jednaki
   • Ako su zbroj i umnožak jednaki ispisati: umnozak i zbroj 2 broja su jednaki
   • U suprotnom ispisati:
   • Umnozak i zbroj 2 broja su razliciti
"""

x = int(input())
y = int(input())

if x * y == x + y:
    print("Umnožak i zbroj 2 broja su jedanki")
else:
    print("Umnožak i zbroj 2 broja su različiti")