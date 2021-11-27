"""
17. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz 
znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od 
unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti 
i ispisati informaciju da je veliko slovo "A" pronađeno.
"""

x = "abCDnDHjKAzhD"

cnt = 0
for c in x:
    if c == 'A':
        print("Slovo A pronađeno.")
        break

    if c >= 'A' and c <= 'Z':
        cnt += 1
    
print(cnt)