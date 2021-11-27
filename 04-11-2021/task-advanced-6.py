"""
6. ROT13 je zapravo specijalan slucaj Cezarove sifre. Cezarova sifra funkcionira na sljedeci nacin:
   Potreban je niz znakova od 26 slova (ili 30 za hrvatski slucaj), koji djeluje kao kljuc sifre.
   Prvo slovo odgovara slovu A, drugo odgovara slovu B i tako dalje.
   Potom se u stringu koji je "zrtva" enkripcije, svako slovo mijenja s odgovarajucim slovom iz kljuca.
   Napravite funkciju enkriptor, te funkciju dekriptor. Pitajte ako nesto nije jasno.

   #Napravi random generator ključa, sprema se u fajl, i čita iz istog.
"""

def _getAlphabet():
    for l in range(ord('a'), ord('z') + 1):
        yield chr(l)

def cesarEncode(phrase, encKey):
    encodedStr = []

    for letter in phrase:
        replacementLetter = encKey[ord(letter) - ord('a')]       
        encodedStr += replacementLetter

    return "".join(encodedStr)

def cesarDecode(phrase, encKey):
    return cesarEncode(phrase, encKey) #sama je sebi inverzna funkcija

testStr = "OvoJeTestnaRecenica".lower()
shift = 13
encryptionKey = "".join([chr(ord('a') + (ord(c) - ord('a') + shift) % 26) for c in _getAlphabet()])

print(cesarEncode(testStr, encryptionKey))
print(cesarDecode(cesarEncode(testStr, encryptionKey), encryptionKey))
