"""
21. Ispišite sljedeće primjere koristeći funkcije i petlju. funkcija mora primati varijabilan broj redaka koji ispisuje (npr. pod a), unesen broj je 7, jer ima 7 redaka. pod b) je unesen broj 5, jer ima 5 redaka)

a)

*
**
***
****
***
**
*

b)

  *  
 *** 
*****
 *** 
  * 
c)
1010101
 10101 
  101  
   1  
d) 
x x x x
x x x
x x
x
x x
x x x
x x x x
"""

def printA(s = 7):
    for i in range(1, s // 2 + 1):
        print('*' * i)
    for i in range(s // 2 + 1, 0, -1):
        print('*' * i)
    print("\n\n")

def printB(s = 3):
    for i in range(s):
        print(('*' * i).rjust(s-1) + '*' + ('*' * i).ljust(s-1))

    for i in range(s-1-1,-1,-1):
        print(('*' * i).rjust(s-1) + '*' + ('*' * i).ljust(s-1))
        
    print("\n\n")

def printC(s = 7):
    sign = True
    for i in range(4):
        for j in range(i):
            print(end=" ")

        sign = True
        for j in range(s - i):
            print("1" if sign else "0", end="")
            sign = not sign

        print()
        s -= 1
    print("\n\n")

def printD(s = 7):
    for i in range(s // 2 + 1, 1, -1):
        print('X' * i)
    for i in range(1, s // 2 + 1 + 1):
        print('X' * i)
   
    print("\n\n")


printA()
printB()
printC()
printD()