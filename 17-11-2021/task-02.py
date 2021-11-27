"""
2. Napravi obrtaljku od unesenog stringa te na svakom drugom mjestu pridruzi nasumičan broj.
"""

x = "Ovo je tekst"

import random

xRev = []
for i, c in enumerate(x[::-1]):
    xRev.append(c)
    if i % 2 == 0: xRev.append(str(random.randint(0, 9)))

print("".join(xRev))