"""
12. Koristeci se principom 'beskonacnog unosa', napravite simulator potapanja brodova. Imate potpunu slobodu u odlucivanju kako ce program izgledati.
"""

from random import *

BOARD_SIZE = 4+1
MAX_ATTEMPTS = 5

def createBoard():
    board = []
    for _ in range(BOARD_SIZE):
        board.append(["o"] * BOARD_SIZE)

    return board

def printBoard(board):
    print("------ Ploča: -------")
    for row in board:
        print(" ".join(row))


board = createBoard()
print(f"Raspon igrače ploče je [0-{BOARD_SIZE-1}]")
print(f"Maksimalni broj pokušaja za potapanje broda je {MAX_ATTEMPTS}")
print("\n")
printBoard(board)

shipRow = randint(0, len(board) - 1) #random row
shipCol = randint(0, len(board[0]) - 1) #random col
print(f"TAJNA: Računalo je namjestilo brod na: ({shipRow}, {shipCol})")

attempt = 0
for attempt in range(MAX_ATTEMPTS):
  print("\n")
  guessRow = int(input("Red: "))
  guessCol = int(input("Stupac: "))

  if guessRow == shipRow and guessCol == shipCol:
      print("Brod potopljen!")
      break
  
  #else
  if (guessRow < 0 or guessRow >= BOARD_SIZE) or (guessCol < 0 or guessCol >= BOARD_SIZE):
    print("Odabrane koordinate su izvan ploče.")
  elif(board[guessRow][guessCol] == "x"):
    print("Opet isti unos...")
  else:
    print("Promašili ste brod")
    board[guessRow][guessCol] = "x"

  print(f"Pokušaj {attempt + 1} \n")
  printBoard(board)
  attempt = attempt + 1

  if attempt == MAX_ATTEMPTS:
    print("Igra gotova")
      