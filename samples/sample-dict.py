d2 = {}  # inicijalizacija praznog rjecnika
d2 = dict({})  # takodjer inicijalizacija praznog rjecnika pomocu funkcije dict

d1 = {"key1": "value1", "key2": 123, "key3": True}  # inicijalizacija rjecnika nekim pocetnim vrijednostima
print("d1: ", d1)

print("keys():", d1.keys())  # vraca listu kljuceva (keys)
print("values():", d1.values())  # vraca listu vrijednosti (values)
print("items():", d1.items())  # vraca tuple za svaki key-value par
print("get():", d1.get("key1"))  # vraca vrijednost (value) unesenog kljuca (key)
d4 = d2.copy()  # kopira rjecnik

t_keys = ("k1", "k2", "k3")
t_value = 0
d3 = d2.fromkeys(t_keys, t_value)  # vraca novi rjecnik sa zadanim kljucevima i JEDNOM vrijednoscu koju postavljamo na te kljuceve
print("fromkeys():", d3)

d3.setdefault("k1")  # vraca vrijednost kljuca ako postoji. kreira novi kljuc sa predanom vrijednosti ako kljuc NE postoji
print("setdefault():", d3)

d1.update({"key1": "IZMIJENJENA_VRIJEDNOST", "new_key1": [1, 2, 3]})  # dodavanje novih parova u rjecnik
print("d1 nakon update():", d1)

d2 = {"d2_key": "update_preko_novog_rjecnika"}
d1.update(d2)
print("d1 nakon update(d2):", d1)

d1.pop("key2")  # uklanja par pod nazivom kljuca
print("d1 nakon pop('key2'):", d1)

d1.popitem()  # uklanja uvijek POSLJEDNJI par iz rjecnika
print("popitem():", d1)

print("\nSPIS PREKO FOR PETLJE...\n")
for key in d1:
    print(f"kljuc {key} ima vrijednost {d1[key]}")

print("\nSPIS PREKO FOR PETLJE KORISTECI FUNKCIJU items()...\n")

for key, value in d1.items():
    print(key, value)


