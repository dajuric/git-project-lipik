"""
6. S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo 
koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo 
veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva 
osim broja zbog kojeg je prekinuto učitavanje.
"""

nSum = 0
nNum = 0

while True:
    n = int(input("Broj: "))
    if n < nNum:
        break

    nNum = n
    nSum += n

print(nSum)