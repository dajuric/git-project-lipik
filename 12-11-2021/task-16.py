sA = "Ovo je prva rečenica i to jako duga."
sB = "Ovo je druga rečenica."

sA = sA.split(); sB = sB.split()
sA = sA[:len(sB)]

dict = {}
for wA, wB in zip(sA, sB):
    dict.update({ wB: wA })

print(dict)

