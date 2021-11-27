"""
14. Ivica ima n kuna za koje želi kupiti prijateljima čokolade. Jedna čokolada stoji m kuna. Ivicu 
zanima koliko će najviše čokolada moći kupiti te koliko će mu novca nakon toga preostati. 
Pomogni Ivici i napiši program koji će unositi iznos novca kojim Ivica raspolaže te cijenu jedne 
čokolade, a ispisivati koliko maksimalno čokolada Ivica može kupiti te koliko će mu novca 
nakon toga ostati. 
"""

n = int(input("Kuna: "))
m = int(input("Jedna čokolada: "))
print(f"Ivica može kupiti najviše: {n // m} čokolada i pri tome mu ostaje: {n % m} kuna.")

