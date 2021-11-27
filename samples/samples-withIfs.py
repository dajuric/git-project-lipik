#%%
x = int(input())
isEven = x % 2
print(isEven)

#%%
x = int(input())
if x % 2:
    print("Broj djeljiv sa 2")
elif x % 3:
    print("Broj djeliv sa tri")
elif x % 5:
    print("Broj djeliv sa 5")

#%%
from typing import *
from functools import reduce

def isSorted(arr: List[int], reverse: bool = False) -> bool:
    isSorted = True
    arrSort = sorted(arr, reverse=reverse)

    for a, b in zip(arr, arrSort):
        if a != b:
            isSorted = False
            break

    return isSorted

x = list(map(int, input().split()))
if len(x) != 3:
    print("Trebate unijeti 3 cijela broja.")
    exit(1)

if isSorted(x, True):
    print(reduce(lambda a, b: a + b, x, 0))
elif isSorted(x, False):
    print(reduce(lambda a, b: a / b, x, 1))
else:
    print(reduce(lambda a, b: a * b, x, 1))
