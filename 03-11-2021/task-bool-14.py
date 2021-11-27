"""
14. Napravite program koji će za unos dva broja vršiti sljedeće operacije: zbrajanje,
oduzimanje, množenje i dijeljenje.
Na početku je potrebno korisniku omogućiti unos dva broja, zatim odabrati operaciju
odabirom znaka te operacije (+,-,*,/)
"""

x = int(input("Broj A: "))
y = int(input("Broj B: "))
op = input("Operacija (+, -, *, /):")

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    print(x / y)
else:
    print("Nepostojeća operacija")