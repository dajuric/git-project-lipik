sentence = "Ovo je neka rečenica i baš me ne sluša." #input("Rečenica: ")
wordList = sentence[:-1].strip().split(" ")

cleanedList = []
for w in wordList:
    if w in ["bar", "baš", "čak", "da", "evo", "eto", "eno", "kao", "li", "ma", "ne", "zar"]:
        continue

    if w in ["i", "pa", "a", "ili"]:
        continue

    cleanedList.append(w)

print(cleanedList)