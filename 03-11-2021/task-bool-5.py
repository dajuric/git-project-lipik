"""
5. • Unesite 2 broja
   • Ako su oba broja jednaka izračunati površinu kvadrata (p=a**2)
   • U suprotnom izračunati površinu pravokutnika (a*b)
"""

x = int(input())
y = int(input())

if x == y:
    print(x ** 2)
else:
    print(x * y)