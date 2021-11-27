"""
8. Napiši program koji traži sequence velikih slova iza kojih se nalaze mala slova.
"""

s = "OVO je Match"

import re
matches = re.findall("[A-Z]+[a-z]+", s)
print(matches)
