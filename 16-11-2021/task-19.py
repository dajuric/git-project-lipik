"""
19. vas omiljeni carobni aparat za kavu je podivljao. aparat treba ispitivati korisnika za kavu sve dok on ne unese "Q" ili 0. aparat prihvaca samo kovanice od 2kn ili 5kn. kada korisnik ubaci kovanicu od 5kn, aparat nausmicno izbacuje dvije kave. kada korisnik ubaci kovanicu od 2kn, aparat nasumicno izbaci jednu kavu. ako aparat sakupi 20kn, on se magicno napuni za 3 kave. neka set sljedeceg oblika simbolizira pocetnu kolicinu kave u aparatu: set_kava = {1, 2, 3, 4, 5, 6}. set se treba umanjivati sa svakom isporucenom kavom.
"""
from random import *

cofee_set = {1, 2, 3, 4, 5, 6}
collected_amount = 0

while True:
    x = input("Upit: ")
    if x.lower() == "q" or x == "0":
        break

    x = int(x)
    if x == 5:
        print(cofee_set.pop())
        print(cofee_set.pop())
        collected_amount += 5
    elif x == 2:
        print(cofee_set.pop())
        collected_amount += 2

    if collected_amount >= 20:
        collected_amount = 0
        cofee_set.update([randint(1, 6) for _ in range(3)])
        