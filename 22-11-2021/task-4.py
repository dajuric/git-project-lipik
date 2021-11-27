"""
4. kreirajte klasu Vozilo, koja sadrzi sljedece atribute: marka, model, masa, kilometraza, max brzina, boja, cijena. napravite 2 objekta sa razlicitim atributima. nakon postavljanja, izmijenite boju u crvenu, kilometrazu postavite na 10000, max brzinu spustite za 15 i cijenu spustite za 10%. usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu. 
"""

class Vehicle():
    def __init__(self, manuf, model, color, mileage, maxSpeed, price) -> None:
        self.manuf = manuf
        self.model = model
        self.color = color
        self.mileage = mileage
        self.maxSpeed = maxSpeed
        self.price = price

a = Vehicle("Mazda",  "A", "red",  1000, 150, 15000)
b = Vehicle("Toyota", "B", "blue", 1500, 120, 12500)

a.color = "red"
a.mileage = 10000
a.maxSpeed -= 15
a.price *= 0.9

print("Auto ima veću max. brzinu: " + a.manuf if a.maxSpeed > b.maxSpeed else b.manuf)
print("Auto ima veću kilometražu: " + a.manuf if a.mileage > b.mileage   else b.manuf)
print("Auto ima manju cijenu:     " + a.manuf if a.price   < b.price     else b.manuf)