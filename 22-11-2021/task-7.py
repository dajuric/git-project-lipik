"""
7. nadogradite program iz prethodnog zadatka tako da napravi i konverziju args-a u liste i setove. napravite metodu koja ce vrsiti trazene operacije sa setovima. neka korisnik preko inputa odluci koju operaciju zeli izvrsiti.
"""

class PrintArgs():

    def __init__(self) -> None:
        pass

    def convertAndArgs(self, *args, toSet = False):      
       converted = None
       if toSet:
           converted = set(args)
       else:
           converted = list(args)

       print(converted)



pa = PrintArgs()
pa.convertAndArgs(1, 2, 3, 4, 5, toSet = False)
pa.convertAndArgs(1, 2, 3, 4, 5, toSet = True)

