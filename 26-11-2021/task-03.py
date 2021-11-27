"""
3. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi jedno ili više 'b'
"""

s = "ldaskabblsllklabbblkllab"

import re
matches = re.findall(r"ab{1,}", s)
print(matches)