"""
11. Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 
20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu 
poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon 
učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
parova brojeva učitano, ispišite parove brojeva koji imaju najveću 
sumu.
"""

n = -1
while True:
    x = input("Broj [3-20]: ")
    try:
        n = int(x)
        if n < 3 or n > 20:
            continue
    except:
        continue

    break

maxSum = 0
while n > 0:
    a, b = input("Dva broja: ").split(" ")

    sum = int(a) + int(b)
    if sum > maxSum:
        maxSum = sum

    n -= 1

print(maxSum)