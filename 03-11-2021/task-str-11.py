"""
11. Napiši program koji unosi jedan troznamenkasti broj i ispisuje znamenku deseticu,stoticu i jedinicu (koristeći isključivo današnje gradivo)
"""

x = int(input("Troznam. broj: "))
if x < 100 or x > 999:
    print("Unešeni broj nije troznamenkasti.")
    exit(1)

x = str(x)
print(x[1], x[0], x[2])