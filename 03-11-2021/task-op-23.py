"""
23. Napisi program koji unosi neki troznamenkasti broj x te ispisuje jedinicu, deseticu i stoticu.
"""

x = int(input("Troznam. broj: "))
if x < 100 or x > 999:
    print("Unešeni broj nije troznam.")
    exit(1)

while x != 0:
    n = x % 10
    print(n, end=" ")
    x = x // 10
