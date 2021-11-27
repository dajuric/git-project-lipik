"""
7. Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova 
spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju 
ista slova neovisno o veličini ('a' i 'A' tretirati jednako).
"""

a = "abcAA"; b = "AhChSJjsakA"

for i, (cA, cB) in enumerate(zip(a, b)): #zip enumerira do najkraćeg niza
    if cA.lower() == cB.lower():
        print(i)