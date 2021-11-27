"""
15. Napišite program koji ispisuje koliko ima prostih brojeva između 
dva proizvoljna broja (prost broj je broj koji je djeljiv samo sa 1 i sa samim sobom).
"""

a = 15; b = 190

cnt = 0
for i in range(a, b+1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        cnt += 1

print(cnt)