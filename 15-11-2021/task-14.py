"""
14. napisi funkciju koja prima rjecnik te vraca najvecu i najmanju vrijednost. raspakiraj vrijednosti te ih ispisi u glavnom dijelu programa. koristi formatiranje stringa.
"""

def minMax(d: dict):
    mA = min(d.values())
    mB = max(d.values())

    return mA, mB


d = {"jedan": 1, "dva": 2, "tri": 3, "četiri": 4}
mA, mB = minMax(d)
print(mA, mB)