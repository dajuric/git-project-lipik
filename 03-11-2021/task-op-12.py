"""
12. Napiši program koji će unositi dva prirodna broja a i b te ispisivati njihov zbroj, razliku, 
umnožak i količnik (drugi je broj uvijek različit od nule). Ispis programa treba biti „punog“ 
oblika, primjerice, za unos brojeva 5 i 7 te operaciju + ispis treba biti 5+7=12. 
"""

a = int(input())
b = int(input())

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")