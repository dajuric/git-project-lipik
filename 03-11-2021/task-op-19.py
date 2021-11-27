"""
19. Izračunati aritmetičku sredinu sedam brojeva
"""

arr = list(map(float, input("Upišite brojeve: ").split()))
if len(arr) != 7:
    print("Treba biti 7 brojeva.")
    exit(1)

x = sum(arr) / len(arr)
print(x)