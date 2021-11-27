"""
15. Napiši program koji traži dvoznamenkaste i troznamenkaste brojeve (0-9) u bilo kojem stringu.
"""

s = "Ovo je neki tekst sa brojevima: 22, 44, 555, 6666, 77777"

import re

pattern = re.compile("\d{2,3}")
matches = pattern.finditer(s)
for m in matches:
    print(m)