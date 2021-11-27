
def printChessPattern(n):

    isBlack = True
    for i in range(n):
        for j in range(n):
            print("█" if isBlack else "░", end = " ")
            isBlack = not isBlack
        print()

printChessPattern(5)

