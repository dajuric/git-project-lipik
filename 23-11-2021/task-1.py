"""
1. napravite klasu Prva i Druga. neka obje imaju po 2 atributa i po jednu metodu za ispis proizvoljnog teksta. izvedite drugu klasu iz prve te ispisite sva 4 atributa koristeci izvedenu klasu.
"""

class First():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + " " + str(self.b)

class Second(First):
    def __init__(self, a, b, c, d) -> None:
        super().__init__(a, b)
        self.c = c
        self.d = d

    def __str__(self):
        base = super().__str__()
        return base + " " + str(self.c) + " " + str(self.d)


s = Second(1, 2, "a", "b")
print(s)
