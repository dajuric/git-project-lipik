"""
6. Napisi program koji iz liste imena
ispisuje najduzu rijec.
"""

l = ["Anaconda", "Python", "A", "Blob"]

maxLen = -1
longestWord = ""

for elem in l:
    eLen = len(elem)
    if eLen > maxLen:
        maxLen = eLen
        longestWord = elem

print(longestWord)