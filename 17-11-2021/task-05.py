"""
5. Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste
"""

l = ["abc", 0, 1, 2, 3, "def", "ghi", 5]

lStr = [x for x in l if isinstance(x, str)]
lNum = [x for x in l if isinstance(x, int)]

print(lStr)
print(lNum)