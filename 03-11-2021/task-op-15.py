"""
15. Napisati program za Pitagorin poučak (izračunati hipotenuzu za unešene vrijednosti kateta).
"""
import math

a, b = map(float, input().split())
c = math.sqrt(a**2 + b**2)
print(c)