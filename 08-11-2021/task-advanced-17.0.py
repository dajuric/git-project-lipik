import re

s = "Ja sam kupio bonboone. Tako sam i ja uživao u njima. Jesi li i ti bio zadovoljan ? Naravno da jesam!"
data = re.split(r' *[\.\?\!] *', s) #https://regex101.com/r/nG1gU7/27

for sentence in data:
    print(sentence)


