"""
18. zadan je rjecnik:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'tinder'],
    'backpack' : ['house key','dagger', 'bedroll','bread loaf']
}
    a) uklonite dagger iz backpack-a
    b) uvecajte gold za 50
    c) uklonite flint i tinder iz pouch i dodajte flint&tinder
    d) kreirajte pocket te smjestite gold i house key u njega
"""

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'tinder'],
    'backpack' : ['house key','dagger', 'bedroll','bread loaf']
}

inventory["backpack"].remove("dagger")
print(inventory)

inventory["gold"] += 50
print(inventory)

inventory['pouch'].remove("flint")
inventory['pouch'].remove("twine")
inventory['pouch'].append("flint&twine")
print(inventory)

inventory["pocket"] = ["gold", "house"]
print(inventory)