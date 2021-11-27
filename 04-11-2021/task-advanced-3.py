"""
3. Napravite program koji ce omoguciti popisivanje knjiga u knjizari. Obavezna su polja 'naslov', 'cijena' i 'godina_izdanja'. Dodajte polja kakva zelite.

#Dodatno: fajl input output radi perzistencije,
# Napravi rendom generator naslova knjiga, cijena te godina izdanja.
"""

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


import os
fd = os.open("knjige.txt", os.O_WRONLY | os.O_CREAT)

while True:
    sample = input("naslov', cijena, godina_izdanja: ")
    if sample == "-1":
        break
    
    if len(sample.split(",")) != 3:
        print("Pogrešan unos")
        continue
    if isInt(sample.split(",")[1]) == False:
        print("Cijena nije broj")
        continue
    if isInt(sample.split(",")[2]) == False:
        print("God. izdanja nije broj")
        continue

    os.write(fd, sample.encode())

os.close(fd)
