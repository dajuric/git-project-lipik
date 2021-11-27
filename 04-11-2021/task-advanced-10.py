"""
10. Koristeci se funkcijom iz 9. i principom 'beskonacnog unosa', napravite simulator automata za prodaju grickalica. Automat mora nuditi bar dva artikla.
"""

def returnMoney(x):
    fiveKunaCount = x // 5
    if fiveKunaCount > 0:
        print(f"Evo {fiveKunaCount} kovanica od 5 kuna.")
    x = x - x // 5 * 5

    twoKunaCount = x // 2
    if twoKunaCount > 0:
        print(f"Evo {twoKunaCount} kovanica od 2 kune.")
    x = x - x // 2 * 2

    oneKunaCount = x // 1
    if oneKunaCount > 0:
        print(f"Evo {oneKunaCount} kovanica od 1 kune.")


snacks = { "Twix": 23, "Mars": 12 }

while True:
    x = input("Produkt: ")
    if x not in snacks.keys():
        print("Nema produkta.")
        continue

    bill = int(input("Novčanica: "))
    reqAmount = snacks[x]

    if bill < reqAmount:
        print("Nedovoljno novca. Molim odaberite nešto drugo.")
        continue

    returnMoney(bill - reqAmount)