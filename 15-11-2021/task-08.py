"""
8. napisi program koji provjerava postoji li neki kljuc u rjecniku.
"""

d = {"1": 1, "2": 4, "3": 9}
print(d.get("1", "ne postoji"))
print(d.get("8", "ne postoji"))