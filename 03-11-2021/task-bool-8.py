"""
8. • Omogućite dva unosa broja 0 ili 1.
   • Upotrijebite operaciju logičkog I
   • Ako je rezultat TRUE ispišite true
   • U suprotnom ispišite FALSE
"""

x = int(input("Broj A (0 ili 1):"))
y = int(input("Broj B (0 ili 1):"))

op = x and y
print(op)