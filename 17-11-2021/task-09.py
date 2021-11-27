"""
9. Napišite program koji učitava cijele brojeve sve dok je unesena 
vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju 
sumu znamenki te ispišite taj broj i sumu.
"""

n = -1
nSum = -1

while True:
    x = input("Broj: ")
    if int(x) <= 0:
        break

    s = sum(int(n) for n in x)
    if s > nSum:
        nSum = s
        n = x

print(f"Broj je {n}, a suma je {nSum}")
