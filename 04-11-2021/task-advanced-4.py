"""
4. Python ima biblioteku 'os', a biblioteka 'os' ima funkciju 'listdir(path)', gdje je 'path' sistemski path do foldera. Napravite program koji ce
ispisati sadrzaj proizvoljnog foldera. Mozete kombinirati s "beskonacnim unosom".

napravljena je rekurzivna fja koja ispisuje sve subdirektorije
"""

from typing import *
import os

def getAllFiles(dir: str) -> List[str]:
    entries = []
    
    try:
        entries = os.listdir(dir)
    except:
        pass

    allFiles = []

    for entry in entries:
        entryFullPath = os.path.join(dir, entry)
        if os.path.isdir(entryFullPath):
            allFiles = allFiles + getAllFiles(entryFullPath)
        else:
            allFiles.append(entryFullPath)

    return allFiles


while True:
    dir = input("Korjenski direktorij: ") # "C:\\Users\\User\\Desktop\\"
    if dir == "-1":
        break

    if os.path.isdir(dir) == False:
        print("Unos nije direktorij.")
        break

    allFiles = getAllFiles(dir)
    for f in allFiles:
        print(f)

    