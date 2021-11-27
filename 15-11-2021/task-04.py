"""
4. koristeci funkciju setdefault(), dohvatite i ispisite ime i prezime iz prethodnog zadatka. koristeci istu funkciju, kreirajte novi par "visina" i pridruzite prikladnu vrijednost.
"""

d = {"ime": "pero", "prezime": "perkovic", "godine": 42, "spol": "M"}

print(d.setdefault("ime", "novo ime"))
print(d.setdefault("prezime", "novo prezime"))
print(d.setdefault("visina", 55))