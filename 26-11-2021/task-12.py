"""
12. Napiši program koji provjerava i vraća rezultat ako se u stringu pojavljuju samo velika i mala slova, brojevi i underscore.
"""

s = "Ovo_je_ispravan_215_string"

import re
pattern = re.compile("[A-Z]+|\d+|_|[a-z]+")
matches = pattern.findall(s)
print(len("".join(matches)) == len(s))