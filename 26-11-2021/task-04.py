"""
4. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi jedno ili dva 'b'
"""

s = "ldaskabblsllklabbblkllab"

import re
matches = re.findall(r"ab{1,2}", s)
print(matches)