"""
6. napravite klasu po zelji. neka jedna metoda prima args, a druga kwargs. u glavnom potprogramu predajte odgovarajuce vrijednosti te ih ispisite.
"""

class PrintArgs():

    def __init__(self) -> None:
        pass

    def printArgs(self, *args, **kwargs):
        print(args)

    def printKWargs(self, **kwArgs):
        print(kwArgs)


pa = PrintArgs()
pa.printArgs(1, 2, 3, 4, 5, a = 10)
pa.printKWargs(a = 10, b = 15, c = 20)