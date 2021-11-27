"""
1. Napiši program koji provjerava sadrži li string određeni set charactera.
    a) a-z 
    b) A-Z 
    c) 0-9
"""

s = "ldaskabblsllklabbblkllabJNDSJKKSA151565156"

import re
matches = re.findall(r"[a-z]+|[A-Z]+|[0-9]+", s)
print(matches)