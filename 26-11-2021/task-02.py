"""
2. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi nula ili više 'b'
"""

s = "ldaskabblsllklabbblkllab"

import re
matches = re.findall(r"ab{0,}", s)
print(matches)