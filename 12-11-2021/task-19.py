nA = input("List A: ").split(",")
nA = list(map(int, nA))

nB = input("List B: ").split(", ")
nB = list(map(int, nB))

tuples = []
for x, y in zip(nA, nB):
    tuples.append((x, y))

tuplesSwitched = []
for x, y in tuples:
    tuplesSwitched.append((y, x))

print(tuplesSwitched)

