"""
3.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
najbolji i najlošiji rezultat.
"""

points = [5, 2, 6, 4, 4, 2, 3, 9]
points = sorted(points)
print(sum(points[1:-1]))