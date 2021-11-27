from functools import reduce

def writeToFile(str, fileName):
    print(str)
    with open(fileName, "a+") as f:
        f.write(str + "\n")

def mul(numbers):
    return reduce(lambda x, y: x * y, numbers)

def sum(numbers):
    return reduce(lambda x, y: x + y, numbers)

def sortDesc(numbers):
    return sorted(numbers, reverse=True)

def getPrimes(numbers):
    primes = []

    for n in numbers:
        isPrime = True
        for i in range(1, n):
            if n % i == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(n)

    return tuple(primes)

def getEvenNums(numbers):
    evenNums = []

    for n in numbers:
        if n % 2 == 0:
            evenNums.append(n)

    return tuple(evenNums)


numbers = [1, 3, 2, 5, 6, 4, 8, 9, 7]
writeToFile(f"Mul:       {mul(numbers)}", "def_rez.txt")
writeToFile(f"Sum:       {sum(numbers)}", "def_rez.txt")
writeToFile(f"SortDesc:  {list(sortDesc(numbers))}", "def_rez.txt")
writeToFile(f"Primes:    {getPrimes(numbers)}", "def_rez.txt")
writeToFile(f"EvenNums:  {getEvenNums(numbers)}", "def_rez.txt")