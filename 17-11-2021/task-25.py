"""
25. napisite funkciju koja prima string oblika "<predmet>, <cijena>, <kolicina>" (npr. "kruh, 7.5, 5"), koji bi simulirao policu neke trgovine. program treba razdvojiti navedeni string te zasebne elemente spremiti u rjecnik. rjecnik se treba spremiti u listu proizvoda. simuliraj kupovinu: kada kupac kupi proizvod (ili broj proizvoda), njegova kolicina se treba umanjiti za iznos. ukoliko je kolicina 0, predmet se treba ukloniti sa police.
"""

def storeInDict(s):
    p, c, k = s.split(", ")
    c = float(c); k = int(k)
    d = {"product": p, "price": c, "amount": k}
    return d

products = [
    storeInDict("kruh, 7.5, 5"),
    storeInDict("čokolada, 15.4, 1")
]

while True:
    reqProduct = input("Produkt: ").strip()
    if reqProduct == "":
        break

    if reqProduct not in [x["product"] for x in products]:
        print("Nema proizvoda.")
        continue

    p = next(filter(lambda x: x["product"] == reqProduct, products))
    p["amount"] -= 1

    if p["amount"] == 0:
        products.remove(p)
