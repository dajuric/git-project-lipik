"""
11. Napisati program za množenje dva broja u rasponu zaključno s brojem 10. Na početku
programa upitati korisnika da li želi množiti brojeve. Ukoliko odgovori pozitivno s da
omogućiti unos i množenje. Ukoliko odgovori negativno, omogućiti izlazak iz programa.
"""

op = input("Množiti brojeve (da/ne) ?")
if op == "ne":
    exit(0)

arr = list(map(int, input("Dva jednoznam. broja: ").split()))
if len(arr) != 2:
    print("Trebate unijeti dva broja.")
    exit(1)

for n in arr:
    if n < 0 or n > 10:
        print("Raspon neodgovarajući.")
        exit(1)

from functools import reduce

prod = reduce(lambda x, y: x * y, arr, 1)
print("Produkt je: " + str(prod))
