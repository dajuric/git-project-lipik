"""
16. Napiši program koji traži određene riječi u stringu:
    Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'
"""

s = 'The quick brown fox jumps over the lazy dog.'

import re
matches = re.finditer("fox|dog|horse", s)
for m in matches:
    print(m)