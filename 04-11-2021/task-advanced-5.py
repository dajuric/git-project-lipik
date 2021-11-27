"""
5. ROT13 je jednostavan algoritam za kriptiranje stringova.
   Svako slovo nekog stringa mijenjamo sa slovom udaljenim 13 mijesta unaprijed,
   ako se slovo nalazi ispod polovine engleske abecede, te 13 mijesta unazad u obrnutom slucaju.
   Napravite funkciju koja ce kriptirati proizvoljni string na takav nacin.
   Napravite funkciju koja ce dekriptirati proizvoljni string na takav nacin.
"""

def _getAlphabet():
    for l in range(ord('a'), ord('z') + 1):
        yield chr(l)

def rot13encode(phrase):
    alphabet = "".join(_getAlphabet())
    encodedStr = []

    for letter in phrase:
        charIdx = ord(letter) - ord('a') #alphabet.find(letter)
        targetIdx = (charIdx + 13) % len(alphabet)
        targetChar = alphabet[targetIdx]
        encodedStr += targetChar

    return "".join(encodedStr)

def rot13decode(phrase):
    return rot13encode(phrase) #sama je sebi inverzna funkcija


testStr = "aOvoJeTestnaRecenica".lower()
print(rot13encode(testStr))
print(rot13decode(rot13encode(testStr)))
