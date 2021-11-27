"""
7. Napravite funkciju koja prima kvadratnu jednadzbu u formatu 'ax^2 + bx + x = 0'
(pri unosu zamijeniti a b i c konkretnim brojevima), te uzvraca s dvjema nul-tockama za specificne slucajeve a b i c.
Pretpostavite da je unos uvijek ispravan.
"""

import re
from math import *

eqStrPattern = re.compile("([0-9]+)x\^2 \+ ([0-9]+)x \+ ([0-9]+) = 0")

eqStr = "16x^2 + 64x + 1 = 0" #input("Upišite kvadratnu jednadžbu: ")
match = eqStrPattern.search(eqStr)
if match == None or len(match.groups()) != 3:
    print("Nevaljani unos.")
    exit(1)

a, b, c = match.groups(); 
a = int(a); b = int(b); c = int(c)

D = b**2 - 4*a*c
if D < 0:
    print("Parabola nema realne nultočke.")
    exit(0)

x1 = (-b + sqrt(D)) / (2*a)
x2 = (-b - sqrt(D)) / (2*a)

print(f"Nultočke parabole su: {x1}, {x2}")