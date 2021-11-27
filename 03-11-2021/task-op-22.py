"""
22. Napisi program koji unosi neki dvoznamenkasti broj x te ispisuje zbroj njegovih znamenki.
"""

x = int(input("Dvoznam. broj: "))
if x < 10 or x > 99:
    print("Unešeni broj nije dvoznam.")
    exit(1)

nSum = 0
while x != 0:
    n = x % 10
    nSum += n
    x = x // 10

print(nSum)