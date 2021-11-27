"""
19. Napiši program koji izbacuje samo brojeve iz nekog URL-a.
"""

urlA = "www.mojUrl252-email2141.com"

import re
urlWithoutNumbers = re.sub("\d+", "", urlA)
print(urlWithoutNumbers)