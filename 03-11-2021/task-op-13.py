"""
13. Napiši program koji će unositi iznos odobreno g potrošačkog kredita c, godišnju kamatnu 
stopu p, broj mjeseci m, a ispisivati kamate prema formuli: k=cp(m+a)/2400 
primjer: 
"""

g, c, p, m = map(float, input().split())
k = c*p*(m+1) / 2400
print(k)

