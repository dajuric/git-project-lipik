"""
17. S tipkovnice uÄitajte proizvoljni niz znakova. Kreirajte novi niz 
znakova koji Ä‡e sadrÅ¾avati naizmjence velika i mala slova iz ulaznog 
niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u 
ulaznom nizu, prvo sljedeÄ‡e malo slovo u nastavku ulaznog niza, 
prvo sljedeÄ‡e veliko slovo u nastavku ulaznog niza itd. Novokreirani 
niz ispiÅ¡ite na zaslon. U nastavku se nalazi primjer:

Ulazni niz: ifeFemFEkej83FkW
Izlazni niz: FeFkFkW
"""

str = "ifeFemFEkej83FkW"
outStr = ""

searchCapital = True
for i in range(len(str)):
    if str[i] >= 'A' and str[i] <= 'Z' and searchCapital:
        outStr += str[i]
        searchCapital = False

    if str[i] >= 'a' and str[i] <= 'z' and not searchCapital:
        outStr += str[i]
        searchCapital = True

print(outStr)