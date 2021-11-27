"""
20. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od
brojeva
"""

newNum = ""
while True:
    x = input("Broj: ")
    if x == "":
        break

    maxDigit = max(x)
    newNum += maxDigit

print(newNum)
