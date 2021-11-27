"""
9. napravite klasu za usitnjavanje ili razmjenu novca. unutar klase osmislite sustav koji bi sadrzavao listu cijelih brojeva (novcanice unutar kase). metoda unutar klase bi primala neki broj. program treba vratiti sumu elemenata liste, koji bi tvorili uneseni broj, odnosno da li je uopce moguce izvratiti tocan iznos, s obzirom na novac u kasi (listi). npr ako je lista [10, 20, 50, 100, 200], a korisnik unese 180kn, program treba izbaciti iz liste 10, 20, 50, 100 te vratiti da je to moguce napraviti.
"""

class ExhangeMoney():

    def __init__(self, bills):
        self.bills = sorted(bills)

    def exhange(self, amount):
        
        if sum(self.bills) < amount:
            print("Nije moguće izvratiti iznos.")
            return False

        toReturn = amount
        for b in self.bills[::-1]:
            if b <= toReturn:
                toReturn -= b
                print(b, end = " ")

        return True


me = ExhangeMoney([10, 20, 50, 100, 200])
me.exhange(70)