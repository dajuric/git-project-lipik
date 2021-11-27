"""
3. Definirajte klasu Vozilo i dvije podklase Auto i Kamion. Sve klase imaju metodu dobaviVrstu koja ispisuje "Auto" za klasu Auto i "Kamion" za klasu Kamion.
"""

class Vehicle():
    def __init__(self, model) -> None:
        self.model = model

    def getModel(self):
        return self.model


class Truck(Vehicle):
    def __init__(self, model) -> None:
        super().__init__(model)


class Car(Vehicle):
    def __init__(self, model) -> None:
        super().__init__(model)


c = Car("Car")
print(c.getModel())