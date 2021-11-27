import re

with open("tekst.txt") as f: s = f.read()
data = re.split(r' *[\.\?\!] *', s) #https://regex101.com/r/nG1gU7/27

for sentence in data:
    print(sentence)