"""
1. napravite klasu Zivotinja. unutar klase definirajte konstruktor koji sadrzi atribute za naziv, tip, masu, vrstu ishrane. definirajte i metodu unutar klase koja ce ispisati navedene atribute. u glavnom potprogramu kreirajte dva razlicita objekta te pozovite kreiranu metodu.
"""

class Animal():
    def __init__(self, name, type, mass, food) -> None:
        self.name = name
        self.type = type
        self.mass = mass
        self.food = food

    def printAttribs(self):
        print(self.name, self.type, self.mass, self.food)


a = Animal("A", "TipA", 50, "hranaA")
b = Animal("B", "TipB", 60, "hranaB")

a.printAttribs()
b.printAttribs()