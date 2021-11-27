"""
14. Unesite dva stringa s1, s2 i ispišite novi string sačinjen od prvog, srednjeg i zadnjeg znaka od oba unesena stringa
"""

s1 = input()
s2 = input()

print(s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1])
