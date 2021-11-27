"""
20. Vlatka je dobila od bake x kuna i odlucila kupiti cokoladice. Svaka cokoladica kosta y kuna.
Napisi program koji ce ucitati koliko je kuna Vlatka dobila i cijenu svake cokoladice te ispisati u
dva retka koliko Vlatka moze kupiti cokoladica za svoj novac i koliko joj je kuna ostalo kad kupi
cokoladice.
"""

n = int(input("Kuna: "))
m = int(input("Jedna čokolada: "))
print(f"Vlatka može kupiti najviše: {n // m} čokolada i pri tome mu ostaje: {n % m} kuna.")
