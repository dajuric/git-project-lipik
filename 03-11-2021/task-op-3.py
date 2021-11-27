"""
3. Napišite program koji će u varijable a i b spremiti dva 
dvoznamenkasta broja. U varijablu a pohranite zadnju znamenku 
broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju 
znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a
i b.
"""

a = 45
b = 67

tmpA = b % 10
b = a % 10
a = tmpA

print(a, b)