"""
2. Ponovno, omogucite unos do trenutka kad je unesen broj -1.
   Program prvo postavlja pitanje - "zelite li napraviti unos?", ako je odgovor 'da', program se nastavlja, ako je 'ne', program se gasi. U slucaju bilo kakvog
   drugog odgovora, ispisuje se poruka o gresci i trazi novi unos.
   Ako korisnik zeli napraviti unos, nudi se unos imena, prezimena, broja godina, spola, najdraza zivotinja, najdraza boja.
   Nakon unosa, program ponovno pita o unosu. Ako je odgovor -1 tokom unosa, prekinuti program i ne dodati uneseno u listu osoba.
   Kad se program iskljuci, (bilo da je odgovor 'ne' ili je unos u nekom trenutku -1), ispisati sve unesene podatke u redcima.

   #Napravi unose permanentnima, čitajući i pišući u fajl.
"""

samples = []

while True:
    query = input("Želite li napraviti unos ? ")
    if query.lower() == "ne":
        break
    
    if query.lower()!= "da":
        print("Greška.")
        exit(1)
      
    sample = input("Ime, prezime, broj godina, spol, najdraža životinja, najdraža boja: ")
    if sample == "-1":
        break
    
    sample = sample.split(",")
    if len(sample) != 6:
        print("Pogrešan unos")
        continue

    samples.append(sample)


for sample in samples:
    print(sample)
