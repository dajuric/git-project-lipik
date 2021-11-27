"""
26. Klara je pronasla jednu staru, neobicnu knjigu. Svaki put kada ju otvori u knjizi nedostaje
nekoliko stranica. Klara vidi npr. na lijevoj strani broj 14, a na desnoj broj 19. Ostale stranice
nedostaju. Ako je a broj stranice na lijevoj strani, a b broj stranice na desnoj strani, na temelju
ulaznih podataka napisi program koji e ispisati i izracunati koliko stranica nedostaje u knjizi.
"""

a = int(input())
b = int(input())
print("Broj stranica koje nedostaju u knjizi je: " + str(b - a - 1))