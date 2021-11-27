"""
1. napravite dva prazna rjecnika dictionary1 i dictionary2 (na oba nacina) i jedan rjecnik popunjen proizvoljnim parovima (min. 3). iz treceg rjecnika napravite sljedece:
    a) ispisite sve kljuceve
    b) ispisite sve vrijednosti
    c) ispisite vrijednost nekog kljuca
    d) ispisite tuple svih kljuceva u rjecniku
"""

dA = dict(); dB = {}; dC = {"ime": "pero", "prezime": "perkovic", "godine": 42}
print(list(dC.keys()))
print(list(dC.values()))
print(dC["godine"])
print(list(dC.items()))