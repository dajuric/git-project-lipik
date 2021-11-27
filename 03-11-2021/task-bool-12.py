"""
12. •Napisati program koji de omoguditi korisniku unos stranica trokuta.
    •Program redom ispisuje stranice trokuta redoslijedom kojim ih je korisnik unio.
    •Program provjerava da li takav trokut postoji. Ako postoji onda
     se provjerava je li trokut jednakostraničan, raznostraničan ili jednakokračan.
    •Nakon provjere, program ispisuje obavijest o postojanju takvog trokuta i vrsti trokuta
    (jednakostraničan, raznostraničan ili jednakokračan.).
    •U suprotnom ispisuje da trokut ne postoji.
"""

arr = list(map(int, input("Stranice trokuta: ").split()))
if len(arr) != 3:
    print("Trebate unijeti tri broja.")
    exit(1)

x, y, z = sorted(arr)
if (x + y > z) == False:
    print("Trokut ne postoji.")
    exit(1)

if x == y == z:
    print("Trokut je jednakostraničan")
elif y == z:
    print("Trokut je jednakokračan")
else:
    print("Trokut je raznostraničan")
