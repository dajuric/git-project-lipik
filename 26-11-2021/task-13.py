"""
13. Napiši program koji miče nule iz IP adresa
"""

ip = "192.108.0.1"

import re
ipWithoutZeros = re.sub("[0]+", "", ip)
print(ipWithoutZeros)