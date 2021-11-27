import os
import re

def addToFile(str, outPath):
    with open(outPath, "a+") as f:
        f.write(str + "\n")

def addToCsv(strings, outPath):
    with open(outPath, "a+") as f:
        f.write(", ".join(strings) + "\n")

def readAllFiles(dir):
    outDir = "extracted_data"
    os.makedirs(outDir, exist_ok=True)

    files = os.listdir(dir)
    for f in files:
         f = os.path.join(dir, f)
         with open(f, "r") as fId: 
             content = fId.read()

         email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content, re.MULTILINE)[0]
         phoneNum = re.search(r'\n(\+?[0-9]+)\n', content).group(1)
         name = re.search("(\w+)[, ]+[0-9]+", content).group(1)
         age = re.search("\w+[, ]+([0-9]+)", content).group(1)
         zodiac = content.split("\n")[1]
         desc = content.replace(email, "").replace(phoneNum, "").replace(name, "").replace(age, "").replace(zodiac, "").strip(" ").strip(",").replace("\n", " ")
       
         addToFile(email, os.path.join(outDir, "emails.txt"))
         addToFile(phoneNum, os.path.join(outDir, "phoneNums.txt"))  
         addToFile(name, os.path.join(outDir, "names.txt"))
         addToFile(age, os.path.join(outDir, "ages.txt"))
         addToFile(zodiac, os.path.join(outDir, "zodiacs.txt"))
         addToFile(desc, os.path.join(outDir, "descriptions.txt"))

         addToCsv([email, phoneNum, name, age, zodiac, desc], os.path.join(outDir, "Tinder.txt"))


readAllFiles("horoskop/")