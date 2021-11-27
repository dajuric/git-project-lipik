"""
13. Napišite program koji će za uneseni broj ispisati da li je broj pozitivan, nula ili negativan
koristeći elif uvjetovanje.
"""

x = int(input())
if x > 0:
    print("Broj je pozitivan.")
elif x < 0:
    print("Broj je negativan")
else:
    print("Broj je 0")