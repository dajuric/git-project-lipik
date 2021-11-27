a = set()  # ovo je set
b = {}  # ovo je dictionary
a1 = {1, 2, 3}  # ovo je set
b1 = {"a": 1, "b": 2, "c": 3}  # ovo je dictionary
print(type(a), type(b))
print(type(a1), type(b1))

me_haz_duplikate = [4, 5, 1, 1, 1, 2, 3, 1, 2, 1, 2, 4, 5, 1, 2, 3]
new_set = set(me_haz_duplikate)
print(new_set)  # mozemo zakljuciti da set izbacuje duplikate. takodjer mozemo zakljuciti da set sortira podatke

"""set ne podrzava indekse i izvlacenje odredjenog elementa putem indeksa"""

for element in new_set:  # prolazak for petljom
    print(element)

if 1 in new_set:
    print(f"{1} se nalazi u setu")

new_set.add("nova_vrijednost")  # .add() dodaje novu vrijednost u set
print(new_set)

old_set = set((99, 88, 77))
new_set.update(old_set)  # .update() dodaje elemente old_set u new_set
print(new_set)

old_list = [101, 202, 303]
new_set.update(old_list)  # .update() moze dodavati i liste, a ne samo setove
print(new_set)

new_set.remove("nova_vrijednost")  # .remove() uklanja postojeci element iz seta; baca error ako ne postoji
print(new_set)

new_set.discard("nova_vrijednost")  # .discard() isto uklanja postojeci element, ali ne baca error ako element ne postoji
print(new_set)

a = {1, 2, 3}
b = {2, 3, 4}
print(f"unija: {a | b}")
print(f"presjek: {a & b}")
print(f"razlika: {a - b} i {b - a}")
print(f"komplement presjeka: {a ^ b}")


