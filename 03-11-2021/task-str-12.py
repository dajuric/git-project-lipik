"""
12. Unesite string neparne duljine veće od 7, te isprintajte novi string sačinjen od srednja 3 znaka zadanog stringa
"""

x = input()
if len(x) <= 7 or len(x) % 2 == 0:
    print("Nevaljani unos.")
    exit(1)

s = len(x) // 2 - 1
e = len(x) // 2 + 1
print(x[s:e+1])