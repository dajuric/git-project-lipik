"""
5. kopirajte rjecnik iz prethodnog zadatka, uklonite posljednji unos, a zatim uklonite "spol". ispisite rjecnik.
"""

d = {"ime": "pero", "prezime": "perkovic", "godine": 42, "spol": "M"}

dCopy = d.copy()
dCopy.popitem()
dCopy.pop("spol", -1)

