sentence = "U kuhinji je stol. STOL je novi."

i = 0
while True:
    s = sentence.lower().find("stol", i)
    if s < 0:
        break

    i += s
    print("Počima na indeksu: " + str(i))