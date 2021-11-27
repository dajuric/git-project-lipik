"""
5. Nadograditi 4 na način da pri pokretanju programa se korisniku nudi izbor:
    1 - dodavanje knjiga
    2 - izlistavanje knjiga
    3 - izlaz iz programa
"""

f = open("knjige.txt", "w+")

choice = input("[D]odati ili [I]izlistati ? ")

if choice == "D":
    while True:
        x = input("Naslov, autor, godina, cijena: ")
        if x == "q":
            break

        f.write(x + "\n")
elif choice == "I":
    data = f.read()
    print(data)
else:
    print("Nevaljani odabir.")

f.close()
