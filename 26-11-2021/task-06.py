"""
6. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi 2 do 3 'b'
"""

s = "ldaskabblsllklabbblkllab"

import re
matches = re.findall("ab{2,3}", s)
print(matches)