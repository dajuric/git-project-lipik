"""
8. Napišite program koji s tipkovnice učitava proizvoljni cijeli 
troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom 
je 121.
"""

x = input("Troznam. broj: ")
if int(x) < 100 or int(x) > 999:
    exit(0)

a = x[0]; b = x[1]; c = x[-1]
maxAC = max([a, c])
print("".join([maxAC, b, maxAC]))
