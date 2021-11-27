"""
9. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojega slijedi bilo što i da završava na 'b'.
"""

s = "kakb ksksksab"

import re
matches = re.findall(".+a.+b$", s)
print(matches)
print(len(matches) != 0)