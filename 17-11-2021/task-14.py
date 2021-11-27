"""
14. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
(stupac) i y (redak) neka budu manje od 10. Program neka ispiše 
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija 
je vrijednost "X". 

Primjer: T=(1,1)
- - - - - - - - - -
- X - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
"""

uC, uR = 1, 5

for r in range(0, 10):
    row = ['-' for _ in range(0, 10)]
    if r == uR: row[uC] = 'X'
    print(" ".join(row))