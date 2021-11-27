"""
20. Prebaci format datuma iz našeg u američki.
"""

usDate = "11/26/2021" # -> 26.11.2021.

import re

pattern = re.compile("(\d+)/(\d+)/(\d+)")
match = pattern.match(usDate)
euDate = f"{match[1]}.{match[2]}.{match[3]}"
print(euDate)