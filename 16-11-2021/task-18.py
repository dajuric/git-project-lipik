"""
18. Nadogradi prethodni zadatak tako da generira dictionary od unesenih elemenata. Pridruzite 0 kao defaultnu vrijednost svim kljucevima
"""

def makeAnotherType(data):
   return {}.fromkeys(data, 0)


print(makeAnotherType([1, 2, 3]))