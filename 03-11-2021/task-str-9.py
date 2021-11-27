"""
9. Napiši program koji unosi rečenicu u 3.licu jednine prezenta i ispisuje ju u prošlom vremenu.  
"""

x = input() #On drži pilu

firstWord = x.split()[0]
secondWord = x.split()[1]

if firstWord.lower() == "on":
    x = "On  je " + secondWord[0:-1] + "ao " + str(x.split()[2:])

elif firstWord.lower() == "ona":
    x = "Ona je " + secondWord[0:-1] + "ala " + str(x.split()[2:])

elif firstWord.lower() == "ono":
    x = "Ono je " + secondWord[0:-1] + "lo " + str(x.split()[2:])

print(x)
