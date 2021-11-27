def printHistogram(n, nBins):

    xmin = min(n); xmax = max(n)
    hist = [0]  * nBins

    for elem in n:
        binIndex = round(((nBins - 1) * (elem - xmin) / (xmax - xmin)))
        hist[binIndex] += 1

    for i, b in enumerate(hist):
        print(f"{i}: " + "#" * b)


n = [2, 1, 7, 6, 6, 2, 2, 1, 3, 4, 2, 6, 1, 4]
printHistogram(n, len(n))
printHistogram(n, 3)

import random
n = random.sample(range(0, 1000), 1000)
printHistogram(n, 3)