import re

strPattern = "abc defg\(x, y, z\)\{.*\}"
r = re.compile(strPattern)

str = "abc defg(x, y, z){ /*neki tekst*/ }"
print("Validan string" if r.search(str) != None else "Krivi unos.")