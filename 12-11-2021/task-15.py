str = "Ovo je rečenica jako duga."
arr = str.split()

for i, w in enumerate(arr):
    if i == 1:
        continue
    if i == len(arr)-1:
        continue

    if i % 2 != 0:
        print(w.lower())
    if i % 2 == 0:
        print("".join(reversed(w)).upper())
    