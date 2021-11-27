import hashlib

m = hashlib.sha256()
m.update(input("Zadaj tekst za enkripciju: ").encode())
print(m.hexdigest())
