"""
3. zadan je rjecnik {"ime": "pero", prezime: "perkovic", godine: 42}. koristeci metodu update, izmijenite vrijednosti rjecnika u vlastito ime, prezime i godine, zatim dodajte novi par "spol" sa prikladnom vrijednosti.
"""

d = {"ime": "pero", "prezime": "perkovic", "godine": 42}

d.update({"ime": "Darko", "prezime": "Jurić"})
d.update({"spol": "M"})
print(d)