"""
22. Napišite program za koji traži najveći zajednički djelitelj dvaju brojeva
"""

a = 9; b = 6

minN = min(a, b)
maxD = 1

for d in range(2, minN):
    if a % d == 0 and b % d == 0:
        maxD = d

print(maxD)