words = ["first", "second", "third", "fourth", "fifth"]

mat = []
for i in range(len(words)):
    t = [0] * len(words)
    t[i] = words[i]
    t = tuple(t)
    mat.append(t)

for t in mat:
    print(t)