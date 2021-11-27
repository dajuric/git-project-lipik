"""
7. Napiši program koji traži sequence malih slova povezanih s 'underscore'.
"""

s = "ovo je neka_sekvenca_napisi_nesto"

import re
#matches = re.findall("\w+_\w+", s)
matches = re.findall("[a-z]+(?:_[a-z]+)+", s) 
print(matches)

#non capturing groups: https://stackoverflow.com/questions/3512471/what-is-a-non-capturing-group-in-regular-expressions