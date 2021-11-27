"""
2. iz prethodne vjezbe iskoristite klasu zivotinja: iz nje izvedite 3 klase (mesojedi, biljojedi, svejedi). iz svake od navedenih klasa izvedite po jednu klasu sa nazivom zivotinje (npr slon, sova, riba). osmislite atribute i metode tako da budu smisleni i neka nesto ispisuju - npr. iz klase mesojed, neka ispise: "hranim se mesom!".
"""

class Animal():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

class Carnivore(Animal):
    def __init__(self, name, meatAmount) -> None:
        super().__init__(name)
        self.meatAmount = meatAmount

    def __str__(self) -> str:
        base = super().__str__()
        return base + " " + str(self.meatAmount)

class Bear(Carnivore):
    def __init__(self, name, meatAmount, species) -> None:
        super().__init__(name, meatAmount)
        self.species = species

    def __str__(self) -> str:
        base = super().__str__()
        return base + " " + str(self.species)

bA = Bear("brundo", 500, "mrki")
print(bA)