"""
13. zadan je rjecnik {'data1':100,'data2':-54,'data3':247}. napisi program koji mnozi sve vrijednosti u njemu.
"""

from functools import reduce

d = {'data1':100,'data2':-54,'data3':247}
print(reduce(lambda x, y: x * y, d.values(), 1))