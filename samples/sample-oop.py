class Vehicle:  # klasa

    def __init__(self, name, weight, price):  # konstruktor
        self.name = name  # definiranje javnog clana
        self.weight = weight
        self.__price = price  # definiranje privatnog clana

    def print_details(self):
        print(f"name: {self.name}")
        print(f"weight: {self.weight}")
        print(f"price: {self.__price}")

    @staticmethod
    def honk(**kwargs):
        print(f"HOOOOOONK, {kwargs['message']} ")

    @staticmethod
    def some_loop(a, *args):
        print("a:", a)
        print("args: ", args)


v1 = Vehicle("auto", 1400, 21000)
v1.print_details()
print(v1.name)  # ispis atributa name
# print(v1.__price)  # ne mozemo dohvatiti clan, jer je privatan
v1.honk(message="SOME MESSAGE")
Vehicle.honk(message="MY NAMEEEEE")
# Vehicle.print_details()
Vehicle.some_loop(3, 9, 8, 7)


def example_default(a, b=10, c=42):
    print("required a: ", a)
    print("default b:", b)
    print("default c:", c)


example_default(4)
 
