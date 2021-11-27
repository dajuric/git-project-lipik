cA = [x for x in "asdfjklč"]
cB = [x for x in "dfklčasx"]
cC = [x for x in "jsdakolsdssdsa"]

arr = cA + cB + cC
commonChars = []

for x in set(arr):
    if x in cA and x in cB and x in cC:
        commonChars.append(x)

print(commonChars)