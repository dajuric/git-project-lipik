"""
11. zadani su skupovi:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
ispitaj da li je jedan skup podskup drugome, odnosno nadskup drugome.
"""

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

if x.issubset(y):
    print("x je pdskup skupa y")
elif y.issubset(x):
    print("y je podskup skupa x")