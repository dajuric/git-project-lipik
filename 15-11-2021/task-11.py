"""
11. napisite program koji bi trazio unos po 2 vrijednosti u dva rjecnika, spojio ih te ispisao spojeni rjecnik.
"""

dA, dB = dict(), dict()

while True:
    x = input()
    if x == "x":
        break

    k, v = x.split()

    if k.startswith("a"):
        dA.update({k: v})
    else:
        dB.update({k: v})

dA.update(dB)
dB.clear()
print(dA)