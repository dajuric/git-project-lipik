"""
4. klasu Geometrijski_lik iz prethodne vjezbe preuredite tako da se iz nje izvode klase za kuglu i valjak. definirajte prikladne metode i atribute za pojedinu klasu. neka u nadklasi (super klasi) bude definiran samo onaj atribut koji se ponavlja u podklasama
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

#class Cylinder(GShape):
#    TODO:....

s = Sphere(5)
print(s.calcSurface())
print(s.calcVolume())
