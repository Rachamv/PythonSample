# Tic Tac Toe game

def show_board(b):
  print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
--- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
--- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")


def check_winner(b):
  # check rows
  for row in b:
    if row[0] == row[1] == row[2] and row[0] != " ":
      print(f"winner: {row[0]}")
      exit()

  # check columns
  for col in range(3):
    if b[0][col] == b[1][col] == b[2][col] and b[0][col] != " ":
      print(f"winner: {b[0][col]}")
      exit()

  # check diagonals
  if b[0][0] == b[1][1] == b[2][2] and b[0][0] != " ":
    print(f"winner: {b[0][0]}")
    exit()
  if b[0][2] == b[1][1] == b[2][0] and b[0][2] != " ":
    print(f"winner: {b[0][2]}")
    exit()


def run():
  # initialize game board
  board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
  ]
  # starting player is X
  # switches after each loop
  player = "X"

  print("Welcome to tic-tac-toe!")
  print("Enter your choices like 1,1 or 2,3")
  show_board(board)

  # Main game loop
  # Gets player input, updates and displays the board, then checks for a winner
  while True:
    choice = input(f"player {player}, where do you want to play? ")
    numbers = choice.split(",")
    row = int(numbers[0]) - 1
    col = int(numbers[1]) - 1
    board[row][col] = player

    show_board(board)
    check_winner(board) # exits the program if there is a winner

    # switch players
    if player == "X":
      player = "O"
    else:
      player = "X"


if __name__ == "__main__":
  run()