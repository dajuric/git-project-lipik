"""
10. Napiši program koji vraća zadnju riječ u stringu, zajedno s opcionalnim punktuacijama
"""

s = "Ovo je neki string.?"

import re
matches = re.findall("(\w+\.?\!?\??)$", s)
for m in matches:
    print(m)