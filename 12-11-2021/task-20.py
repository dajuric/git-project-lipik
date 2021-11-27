def sortLists(nA, nB):
    indexList = list(range(len(nA)))
    indexList.sort(key = lambda x: nB[x])

    nA = [nA[x] for x in indexList]
    nB = [nB[x] for x in indexList]

    print(nA)
    print(nB)


#nA = [1,     5,  7,    4,   9]
#nB = ["a", "b", "d", "z", "f"]

nA = []; nB = []
while True:
    str = input("A, B: ")
    if str == "-1":
        break

    x, y = str.split(",")
    nA.append(x.strip()); nB.append(y.strip())

sortLists(nA, nB)
