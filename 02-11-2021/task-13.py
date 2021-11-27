"""
13. Varijabli x pridruzi jedan paran broj te ispisi sljedeci po redu paran broj.
"""

x = int(input())
if x % 2 != 0:
    print("Unešeni broj nije paran broj.")
    exit(1)

print("Sljedeći paran broj broja " + str(x) + " je: " + str(x + 2))