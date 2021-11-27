"""
24. Napisi program koji ucitava troznamenkasti broj x te ispisuje novi broj u kojemu su znamenke jedinica i stotica zamijenile mjesta. 
Npr. ako imamo broj 239 i zamijenimo mjesto jedinice i stotice dobit cemo broj: 932.
"""

x = int(input("Troznam. broj: "))
if x < 100 or x > 999:
    print("Unešeni broj nije troznam.")
    exit(1)

a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10

print(f"{a}{b}{c}")