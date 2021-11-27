"""
70. kreirajte password generator, koji mora sadrzavati sljedece funkcionalnosti:
    a) prilikom generiranja treba prikupiti sljedece podatke od korisnika:
        - koliko lozinki zeli napraviti
        - da li da koristi slova, brojeve, simbole
        - duljinu lozinke
        - kapitalizaciju
    b) nadogradite program tako da korisnik upise rijec (hint). od hint se treba ubaciti u nasumicnom redosljedu i kapitalizaciji u lozinku koja se generira
"""

import random

nonCapLetters = [chr(x) for x in range(ord('a'), ord('z'))]
capLetters    = [chr(x) for x in range(ord('A'), ord('Z'))]
numbers       = [chr(x) for x in range(ord('0'), ord('9'))]
symbols       = [chr(x) for x in range(33, 47)]


passwordCount = int(input("Broj lozinki: "))
usedSymbols   = input("Simboli: letters, capLetters, numbers, symbols: ")
passwordLen   = int(input("Duljina lozinke (bez hinta): "))
hint          = input("Hint: ")

pickList = []
if usedSymbols.find("letters") >= 0:
    pickList += nonCapLetters
if usedSymbols.find("capLetters") >= 0:
    pickList += capLetters
if usedSymbols.find("numbers") >= 0:
    pickList += numbers
if usedSymbols.find("symbols") >= 0:
    pickList += symbols

for pIdx in range(passwordCount):
    random.shuffle(pickList)
    passwd = pickList[0:passwordLen]

    hintIdx = random.randint(0, len(passwd))
    passwd = "".join(passwd[0:hintIdx]) + hint + "".join(passwd[hintIdx:])
    print(passwd)
