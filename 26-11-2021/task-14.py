"""
14. Napiši program koji traži postoji li broj na kraju stringa
"""

s = "Ovo je string 234 gdje je na kraju broj: 512"

import re
pattern = re.compile("\d+$")
print(len(pattern.findall(s)) != 0)