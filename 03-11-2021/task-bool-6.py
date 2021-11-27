"""
6. • Upišite neku riječ.
   • Zatim provjerite ako se u toj riječi nalazi samoglasnik a
   • Ako postoji, ispisati samoglasnik se nalazi u napisanoj rijeci, u suprotnom ispisati
nema samoglasnika (koristiti operator istovjetnosti)
"""

x = input()
containsA = 'a' in x.lower()
if containsA:
    print("Samoglasnik se nalazi u napisanoj riječi")
else:
    print("nema samoglasnika")