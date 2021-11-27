"""
5. napravite klasu Banka. definirajte atribute korisnika u obliku rjecnika (oib, ime, prezime, stanje racuna, mjesecni prihod, ima li osiguranje). napravite metodu za podizanje kredita. metoda mora provjeriti da li je stanje racuna pozitivno, jesu li mjesecni prihodi visi od 5% od ukupne trazene svote kredite. ukoliko jesu, metoda vraca True. napravite metodu koja bi izracunala koliko bi mjeseci (i godina) bilo potrebno da korisnik vrati novac. nadogradite program tako da racuna i kamate na godisnjoj razini te ispisite rezultat.
"""

import math

class Bank():
    def __init__(self, ) -> None:
        self.users = []

    def addUser(self, oib, name, accountAmount, monthlyIncome):
        user = { "oib": oib, "name": name, "accountAmount": accountAmount, "monthlyIncome": monthlyIncome }
        self.users.append(user)

    def getLoan(self, oib, requestedLoan):
        user = next(x for x in self.users if x["oib"] == oib)
        if user  == None:
            return False

        return user["accountAmount"] > 0 and user["monthlyIncome"] > 0.05 * requestedLoan

    def getReturnEstimate(self, requestedLoan, monhtlyIncome):
        monthlyReturn = monhtlyIncome * 0.25
        noMonths = math.ceil(requestedLoan / monthlyReturn)

        print(f"Treba {noMonths // 12} godina i {noMonths % 12} mjeseci za vračanje kredita.")
        return noMonths

    def calcInterestRate(self, principal, rate, timeInYrs):
        return principal * (1 + rate * timeInYrs)


b = Bank()
b.addUser(564, "Darko", 20000, 2500)
b.getLoan(564, 50000)
b.getReturnEstimate(50000, 2500)
b.calcInterestRate(50000, 0.11, 1)