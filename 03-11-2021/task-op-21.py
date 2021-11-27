"""
21. Napisi program koji unosi neki dvoznamenkasti broj x i ispisuje znamenku jedinicu i deseticu, jedno ispod drugoga.
"""

x = int(input())
if x < 0 or x > 99:
    print("Samo 2 znam broj.")
    exit(1)

print(x % 10)
print((x // 10) % 10)