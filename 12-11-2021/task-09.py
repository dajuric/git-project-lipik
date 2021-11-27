import random

seconds = random.randint(0, 86400)
h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
print(f"Broj {seconds} je točno {h} sati, {m} minuta i {s} sekundi.")