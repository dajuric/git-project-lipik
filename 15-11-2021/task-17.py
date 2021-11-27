"""
17. napravite program koji zahtijeva ucitavanje imena, prezimena i godina ako korisnik unese 1 te ponavljati unos dok god se ne unese 0. program sprema podatke u rjecnik. kad korisnik unese broj 2, program treba traziti od unos prezimena te ispisati nalazi li se navedeno prezime u rjecniku. ako da, program treba ispisati podatke unesenog korisnika u obliku: "kosnisnik <ime> <prezime> se nalazi u bazi i ima <godine> godina. ukoliko se korisnik ne nalazi u bazi, program treba ispisati odgovarajucu poruku te pitati korisnika zeli li ponovno pretrazivati bazu ili izaci. ako korisnik odabere izlazak, program zavrsava sa izvodjenjem. ukoliko korisnik odabere trecu opciju, program treba ispisati sve spremljene korisnike u formatiranom stringu.
"""

d = dict()

while True:
    x = input("Ime, prezime, godine  (0: izlaz, 2: pretraćivanje po prezimenu): ")
    if x == "-1":
        continue
    if x == "0":
        break
    if x == "2":
        surname = input("Prezime: ")
        data = d.get(surname, None)
        if data == None:
            print("korisnik nije u bazi")
            continue
        else:
            print(f"korisnik: {data[0]}, {surname} se nalazi u bazi i ima {data[1]} godina.")

    name, surname, age = x.split(",")
    d[surname.strip()] = (name, age)

print(d)
