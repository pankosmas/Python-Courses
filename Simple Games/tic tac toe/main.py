# Tic Tac Toe game

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Print initial board
print("  +---+---+---+")
print("2 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
print("1 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
print("0 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
print("  +---+---+---+")
print("    0   1   2  ")

# Change turn
player = "X"

for _ in range(9):
    if player == "X":
        player = "O"
    else:
        player = "X"

    # user input
    print("Player " + player + " plays!")

    while True:
        row = int(input("Give row (0-2) :"))
        col = int(input("Give col (0-2) :"))

        if row < 0 or row > 2:
            print("Row out of bounds!")
            continue
        elif col < 0 or col > 2:
            print("Col out of bounds!")
            continue
        elif board[row][col] != " ":
            print("Pick an empty box!")
            continue
        else:
            board[row][col] = player
            break

    # print board refreshed

    print("  +---+---+---+")
    print("2 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("1 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("0 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2  ")

    # check winner
    winner = False

    if (board[0][0] == board[0][1] and board[0][1] == board[0][2]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != " ":
        winner = player
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]) and board[0][0] != " ":
        winner = player
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]) and board[0][1] != " ":
        winner = player
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]) and board[0][2] != " ":
        winner = player
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[1][1] != " ":
        winner = player
    elif (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[1][1] != " ":
        winner = player

    if winner:
        print("  +---+---+---+")
        print("2 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
        print("1 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
        print("0 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
        print("  +---+---+---+")
        print("    0   1   2  ")
        print("Player " + player + " wins!")
        break

else:
    print("  +---+---+---+")
    print("2 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("1 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("0 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2  ")
    print("We have draw!")
