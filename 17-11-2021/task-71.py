"""
71. napravite tipicnog "chat bota" neke drzavne firme. bot treba primati input korisnika te ako se odredjena rijec u stringu poklapa sa nekim od njemu predefiniranih stringova ili rijeci, ispisati odgovarajucu poruku. npr. ako je korisnik unio "pozdrav, ja sam Alen i radim za mirovinsko osiguranje". bot treba kao prvi string ispisati: "pozdrav, ja sam bot i napravljen pomocu AI", zatim (zbog rijeci mirovinsko), ispisati: " hrvatski zavod za mirovinsko osiguranje je trenutno na pauzi". unesite po zelji 20ak razlicitih stringova te simulirajte neki razgovor/temu po zelji.
"""

def responseMatchesUserInput(userInput, response):
    for x in userInput.split():
        if x in response.split():
            return True

    return False


responses = [
    "pozdrav, ja sam bot i napravljen pomocu AI",
    "hrvatski zavod za mirovinsko osiguranje je trenutno na pauzi",
    "Alen nije zaposlenik mirovinskog osigranja",
    "neki nausmični odgovor koji neće biti upotrebljen"
]

while True:
    userInput = input("Upit: ")
    if userInput == "":
        break

    botResponses = [r for r in responses if responseMatchesUserInput(userInput, r)]
    print(botResponses)