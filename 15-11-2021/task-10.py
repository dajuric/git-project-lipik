"""
10. napisite funkciju koja prima rjecnik te generira broj izmedju 1 i n na mjestu kljuca, odnosno u obliku (x, x*x). npr. ako je zadan n = 3, ispis treba biti: {1: 1, 2: 4, 3:9}
"""

def generateN(d, n):
    for x in range(1, n+1):
        d[x] = x**2

d = {}
generateN(d, 3)
print(d)