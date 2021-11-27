"""
12. napisite funkciju koja zbraja sve vrijednosti unutar rjecnika {"1": 1, "2": 2, "3": 3, "4": 4}
"""

from functools import reduce

d = {"1": 1, "2": 2, "3": 3, "4": 4}
print(reduce(lambda x, y: x + y, d.values(), 0))