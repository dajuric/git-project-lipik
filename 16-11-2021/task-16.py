"""
16. napisi funkciju koja prima dva skupa razlicitih duljina A i B. ako je neki od ta dva skupa podskup drugome, ispisi razliku tih dvaju skupova (od nadskupa oduzmi podskup); ako nisu, napravi uniju i presjek skupova.
"""

def makeSomethingWithSets(a: set, b: set):
    if a.issubset(b):
        print(b - a)
    elif b.issubset(a):
        print(a - b)
    else:
        print(a | b)
        print(a & b)

makeSomethingWithSets({1, 2, 3}, {1, 2, 3, 4})

    