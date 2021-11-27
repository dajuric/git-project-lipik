"""
23. Napisi program koji unosi (naredba input) jedan parni broj x i ispisuje sljedeci parni broj.
"""

x = int(input())
if x % 2 != 0:
    print("Unešeni broj nije paran broj.")
    exit(1)

print("Sljedeći paran broj je: " + str(x + 2))