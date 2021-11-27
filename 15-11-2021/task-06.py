"""
6. koristeci for petlju, ispisite rjecnik (oba nacina)
"""

d = {"1": 1, "2": 4, "3": 9}
for k, v in d.items():
    print(k, v)

for k in d:
    print(d[k])