"""
2. napravite klasu za Obrada_stringa. klasa treba imati mogucnosti da iz nekog stringa napravi sljedece (u obliku metoda):
    a) svaku rijec spremi u listu
    b) ispisuje broj velikih i malih slova, brojeva, znakova
    c) pretvorbu cijelih brojeva u rimske ekvivalente
    d) unazadno ispisuje rijec po rijec (npr ako je uneseno "ja sam" treba ispisati "aj mas")
    e) preoblicavanje slova, koja sadrzi sljedece funkcionalnosti: kapitalizacija svakog slova, uppercase cijelog stringa, spajanje stringa u jednu rijec i mijesanje slova
    f) filtriranje brojeva ili slova, ovisno o trazenom
napravite objekte, pozovite i testirajte program.
"""

from collections import OrderedDict

class ChangeString():
    def __init__(self, s: str) -> None:
        self.s = s

    def toList(self):
        return list(self.s.split())

    def countChars(self):
        return len(self.s)

    def toRomanNumber(self):
        # https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num <= 0:
                    break

        num = 0
        try:
            num = int(self.s)
        except:
            pass

        return "".join([a for a in roman_num(num)])

    def reverseWords(self):
        return [x[::-1] for x in self.s.split()[::-1]]

    def toUppercase(self):
        return self.s.upper()

    def titleWords(self):
        self.s.title()

    def removeSpaces(self):
        return self.s.replace(" ", "")
    
    def filterNumbers(self):
        return [int(x) for x in self.s.split() if x.isdigit()]


csA = ChangeString("Ovo je neki string")
csB = ChangeString("12345")

print(csA.filterNumbers())
print(csA.removeSpaces())
print(csA.reverseWords())

print(csB.toRomanNumber())
