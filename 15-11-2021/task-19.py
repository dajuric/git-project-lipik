"""
19. napisite funkciju koja prima string oblika "<predmet>, <cijena>, <kolicina>" (npr. "kruh, 7.5, 5"), koji bi simulirao policu neke trgovine. program treba razdvojiti navedeni string te zasebne elemente spremiti u rjecnik. rjecnik se treba spremiti u listu proizvoda.
"""

def addToDict(dictList, str):
    a, b, c = str.split(", ")
    dictList.append({a: (float(b), int(c))})


dictList = []
addToDict(dictList, "kruh,   7.5, 5")
addToDict(dictList, "mljeko, 8.5, 6")

print(dictList)