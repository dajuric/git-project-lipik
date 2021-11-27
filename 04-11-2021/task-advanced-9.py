"""
9. Napravite funkciju koja simulira automat za usitnjavanje novca. Korisnik unosi novcanice od 10, 20, 50, 100, 200, 500 ili 1000 kuna,
   a program uzvraca broj kovanica od 5, 2, ili 1 kunu, te ispis koliko kojih kovanica vraca.

   #dodatno: Ograničiti broj kovanica za svaku kovanicu koji automat može vratiti. Ako ne može, ispisati "NEMA DOVOLJNO KOVANICA"
"""

def returnMoney(x):
    fiveKunaCount = x // 5
    if fiveKunaCount > 0:
        print(f"Evo {fiveKunaCount} kovanica od 5 kuna.")
    x = x - x // 5 * 5

    twoKunaCount = x // 2
    if twoKunaCount > 0:
        print(f"Evo {twoKunaCount} kovanica od 2 kune.")
    x = x - x // 2 * 2

    oneKunaCount = x // 1
    if oneKunaCount > 0:
        print(f"Evo {oneKunaCount} kovanica od 1 kune.")

x = 1001 #int(input())
returnMoney(x)