"""
10. Ispišite sljedeće primjere koristeći while petlju:

a)

*
**
***
****

b)

  *  
 *** 
*****
 *** 
  * 
c)
1010101
-10101 
--101  
---1  
"""

s = 4
for i in range(s+1):
    print('*' * i) 
print("\n\n"); 


s = 3
for i in range(s):
    print(('*' * i).rjust(s-1) + '*' + ('*' * i).ljust(s-1))
for i in range(s-1-1,-1,-1):
    print(('*' * i).rjust(s-1) + '*' + ('*' * i).ljust(s-1))
print("\n\n"); 


sign = True; k  = 7
for i in range(4):
    for j in range(i):
        print(end=" ")

    sign = True
    for j in range(k - i):
        print("1" if sign else "0", end="")
        sign = not sign

    print()
    k -= 1
