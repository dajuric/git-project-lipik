"""
19. Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara novi broj.
"""

newNum = ""
while True:
    x = input("Broj: ")
    if x == "":
        break

    tenDigit = x[-2] if len(x) >= 2 else 0
    newNum += tenDigit

print(newNum)