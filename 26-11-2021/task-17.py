"""
17. Za svaku riječ iz zadatka 16. izbaci i od kojeg do kojeg indeksa se pojavljuju
"""

s = 'The quick brown fox jumps over the lazy dog.'

import re
sResult = re.sub("fox|dog|horse", "", s)
print(sResult)