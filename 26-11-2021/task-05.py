"""
5. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi 3 'b'
"""

s = "ldaskabblsllklabbblkllab"

import re
matches = re.findall(r"ab{3}", s)
print(matches)