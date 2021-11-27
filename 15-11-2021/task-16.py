"""
16. Napravite hrvatsko-engleski rječnik. Ključ podataka neka bude hrvatska riječ, a vrijednost toga ključa neka bude engleska riječ. Napuniti rječnik s 5 elemenata. Napraviti beskonačnu petlju koja učitava s tipkovnice hrvatske riječi. Za svaku učitanu riječ (ako prijevod postoji) ispisati prijevod, a ako tražena riječ ne postoji, ispisati poruku da ta riječ ne postoji u rječniku. Učitavanje raditi tako dugo dok se ne unese znak 'x'. Potrebno je obratiti pažnju na mala/velika slova. Prijedlog je pretvarati sve u mala slova.
"""

d = {"stol": "table", "stolica": "chair", "majica": "shirt", "računalo": "computer"}

while True:
    x = input("HRV riječ: ")
    if x == "x":
        break

    x = x.lower()
    translation = d.get(x, "prijevod ne postoji")
    print(translation)