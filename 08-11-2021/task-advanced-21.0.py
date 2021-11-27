from math import floor, sqrt

def std(n):
    mean =sum(n)/len(n)
    SUM= 0
    for i in n :
        SUM +=(i-mean)**2

    stdeV = sqrt(SUM/len(n))
    return stdeV

def mean(n):
    return sum(n) / len(n)

def median(n):
    n = sorted(n)
    return n[len(n) // 2]

def quartiles(n):
    posA = floor(1 * (len(n) + 1) / 4 - 1)
    posB = floor(1 * (len(n) + 1) / 2 - 1)
    posC = floor(3 * (len(n) + 1) / 4 - 1)

    n = sorted(n)
    return n[posA], n[posB], n[posC]

def range(n):
    return (min(n), max(n))


arr = [5, 4, 1, 2, 3, 7, 8, 9]
print("Std: " + str(std(arr)))
print("Mean: " + str(mean(arr)))
print("Median: " + str(median(arr)))
print("Quartiles: " + str(quartiles(arr)))
print("Range: " + str(range(arr)))

