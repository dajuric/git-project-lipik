""" 
def five():
    space = 3

    rows = []
    rows.append('*' + ' ' * space + '*')
    rows.append(' ' * (space // 2 + 1) + '*' + ' ' * (space // 2))
    rows.append('*' + ' ' * space + '*')
    return rows 
"""

def five(size, buildingBlock):
    rows = []

    shouldWrite = True
    for i in range(size):
        mat = [[] for _ in buildingBlock]

        #five
        for j in range(0, size):
            for r, b in zip(mat, buildingBlock):
                r.append(b if shouldWrite else ' ' * len(b))
            shouldWrite = not shouldWrite

        for r in mat:
            rows.append("".join(r))

    return rows


a = five(3, ['*-----*', '---*---', '*-----*'])
b = five(3, a)
for r in b:
    print(r)


