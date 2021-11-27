"""
13. Unesite dva stringa s1, s2, te kreirajte novi string tako što ćete postaviti s2 u sredinu s1
"""

x = input()
y = input()

b = round(len(x) / 2)
print(x[0:b] + y + x[b:])