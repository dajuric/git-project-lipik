"""
8. Pomocu 'beskonacnog unosa', napravite kalkulator. Kalkulator prima izraze tipa 'x + y', te vraca rezultat.
#Nadogradnja: implementirajte zagrade.
"""

import re

inputStrPattern = re.compile("([0-9]+) (.*) ([0-9]+)")

while True:
    x = input()
    if x == "":
        break

    match = inputStrPattern.search(x)
    if match == None or len(match.groups()) != 3:
        print("Nevaljani unos.")
        continue

    a, op, b = match.groups()
    a = int(a); b = int(b)

    if op == "+":
        print(f"{a} + {b} = {a+b}")
    elif op == "-":
        print(f"{a} - {b} = {a-b}")
    elif op == "*":
        print(f"{a} * {b} = {a*b}")
    elif op == "/":
        print(f"{a} / {b} = {a/b}")
    else:
        print("Nevaljani operator")