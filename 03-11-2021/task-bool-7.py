"""
7. •Unesite broj. Ako je unesen broj 1 omoguci operaciju zbrajanja dva broja i ispiši zbroj;
   •Unosom bilo kojeg drugog broja omoguci operaciju množenja dva broja
   i ispiši umnožak
"""

op = int(input("Operacija (kao broj): "))
nA = int(input("Broj A: "))
nB = int(input("Broj B: "))

if op == 1:
    print(nA + nB)
else:
    print(nA * nB)