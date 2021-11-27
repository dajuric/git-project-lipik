"""
18. Pronađi sve substringove 'exercises' u 'Python exercises, PHP exercises, C# exercises'.
"""

s = 'Python exercises, PHP exercises, C# exercises'

import re
matches = re.finditer("exercises", s)
for m in matches:
    print(m)


