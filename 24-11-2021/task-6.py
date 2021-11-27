"""
6. Nadograditi 5 na način da prije izbornika pita korisnika za žanr knjiga koji želi obrađivati.
Svaki žanr je pohranjen u svojoj datoteci. Kad korisnik unese žanr, ostatak programa se pokreće
i vrši se obrada nad tom datotekom.
"""

def processFile(genre):
    f = open(f"{genre}.txt", "w+")

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


genreChoice = input("Žanr: ")
processFile(genreChoice)