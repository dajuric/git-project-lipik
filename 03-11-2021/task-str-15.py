"""
15. Nađite sva pojavljanja ‘stol’ u zadanom stringu zanemarujući velika i mala slova: „U kuhinji je stol. STOL je novi.”
"""

sub = "stol"
x = "U kuhinji je stol. STOL je novi."
x = x.lower()


from typing import *

def findAllSubstrings(str: str, subStr: str) -> List[int]:
    s = 0
    while True:
        s = str.find(subStr, s)
        if s == -1: break
        yield s
        s += len(subStr)

allIndices = findAllSubstrings(x, sub)
print("Svi indeksi su: " + str(list(allIndices)))

