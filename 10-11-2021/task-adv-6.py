""" 
def triangle(size):
    rows = []
    for i in range(size):
        row = []
        for j in range(i + 1, size):
            row.append(" ")
        for j in range(2 * i + 1):
            row.append("*")
        for j in range(i + 1, size):
            row.append(" ")           
        rows.append("".join(row))
    return rows 
"""

def triangle(size, buildBlock):
    rowsStr = []
    for i in range(size):
        mat = [[] for _ in buildBlock]

        #razmak prije
        for j in range(i + 1, size):
            for r, b in zip(mat, buildBlock):
                r.append(" " * len(b)) #dodaj u redak

        #trokut (ili building block)
        for j in range(2 * i + 1):
            for r, b in zip(mat, buildBlock):
                r.append(b if j % 2 == 0 else " " * len(b)) #dodaj u redak

        #razmak poslije
        for j in range(i + 1, size):
            for r, b in zip(mat, buildBlock):
                r.append(" " * len(b)) #dodaj u redak

        for r in mat:
            rowsStr.append("".join(r))

    return rowsStr


a = triangle(3, ['*'])
b = triangle(3, a)
for row in b:
    print(row)
