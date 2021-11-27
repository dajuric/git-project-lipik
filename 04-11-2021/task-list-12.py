"""
12. NapiÅ¡i program koji uÄitava listu i briÅ¡e sve duplikate iz te liste te ispisuje novu listu s 
obrisanim duplikatima.
"""

l = ["a", "b", "c", "d", "a", "b"]

uniqueList = []
for letter in l:
    if letter not in uniqueList:
        uniqueList.append(letter)

print(uniqueList)