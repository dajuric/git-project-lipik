"""
11. Napiši program koji vraća sve riječi koje sadrže 'z'
"""

s = 'The quick brown fox jumps over the lazy dog.'

import re
matches = re.finditer("[a-zA-Z]*z[a-zA-Z]*", s)
for m in matches:
    print(m)