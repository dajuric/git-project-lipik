"""
12. zadani su skupovi:
A = {1, 5, 1, 5, 4, 7, 8, 2, 3, 2}
B = {1, 2, 3, 6}

ispisite sljedece: 
    a) uniju 
    b) presjek
    c) razliku
    d) komplement presjeka
"""

A = {1, 5, 1, 5, 4, 7, 8, 2, 3, 2}
B = {1, 2, 3, 6}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)