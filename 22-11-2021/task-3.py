"""
3. napravite klasu Geometrijski_lik. klasa treba imati mogucnost proracuna oplosja i obujma kugle, valjka i kvadra te ispis navedenih oplosja te koristenih formula za proracun. ispisite na ekran sve navedeno.
"""

import math

class GShape():
    def __init__(self) -> None:
        pass

    def calcSurface(self):
        pass

    def calcVolume(self):
        pass

class Sphere(GShape):
    def __init__(self, r) -> None:
        super().__init__()
        self.r = r

    def calcSurface(self):
        super().calcSurface()
        return 4 * math.pow(self.r, 2) * math.pi

    def calcVolume(self):
        super().calcVolume()
        return 4/3 * math.pow(self.r, 3) * math.pi

#class Square(GShape):
#    TODO:....

s = Sphere(5)
print(s.calcSurface())
print(s.calcVolume())

    