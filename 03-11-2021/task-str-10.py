"""
10. Napiši program koji unosi jedan troznamenkasti broj i ispisuje zbroj njegovih znamenki.
"""

x = int(input("Troznam. broj: "))
if x < 100 or x > 999:
    print("Unešeni broj nije troznamenkasti.")
    exit(1)

nSum = 0
while x != 0:
    n = x % 10
    nSum += n
    x = x // 10

print(nSum)