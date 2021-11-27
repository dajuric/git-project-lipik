"""
11. Implementirajte matrice pomocu lista. Matrice promotrimo kao 2D liste. Redci matrice ce biti pod-liste glavne liste.
    Primjer matrice:

    a11 a12 ... a1j
    a21	a22 	.
    a31 ...	.
    .		.
    .		.
    ai1.........aij

    Neobaveznim redosljedom.
    Napravite funkciju koja ce isprintati matricu na takav nacin.
    Napravite funkciju za dohvat (i, j) clana matrice.
    Napravite funkciju koja ce transponirati matricu.
    Napravite funkciju koja ce ispisati dimenzije matrice.
"""

from typing import *

class Matrix:
    def __init__(self, nRows: int, nCols: int):
        self._mat = []

        for r in range(nRows):
           self._mat.append([])
           for c in range(nCols):
              self._mat[r].append(0)

    def print(self):
        for r in self._mat:
            print(r)

        print()

    def getElement(self, r: int, c: int):
        if r >= len(self._mat):
            raise IndexError("Row out of range")

        col = self._mat[c]
        if c >= len(col):
            raise IndexError("Column oout of range") 

        return self._mat[r][c]

    def transpose(self):
        nRows = len(self._mat)
        nCols = len(self._mat[0])
        t = Matrix(nCols, nRows) 

        for r in range(nRows):
            for c in range(nCols):
                t._mat[c][r] = self._mat[r][c]

        return t

    def __add__(self, otherNum):
        nRows = len(self._mat)
        nCols = len(self._mat[0])

        result = Matrix(nRows, nCols) 
        for r in range(nRows):
            for c in range(nCols):
                result._mat[r][c] = self._mat[r][c] + otherNum

        return result

#*************** test ******************
mat = Matrix(0, 0)
mat._mat = [[1, 2, 3], [4, 5, 6], [7,8,9]]
mat.print()

v = mat + 5
v.print()

e = mat.getElement(2, 1)
print("")
print(f"Element je {e}")

print("")
tMat = mat.transpose()
tMat.print()
