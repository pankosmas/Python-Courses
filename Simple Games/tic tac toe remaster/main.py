# This is a sample Python script.
# Tic Tac Toe game

# globals
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# functions


def print_board():
    print("  +---+---+---+")
    print("2 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("1 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("0 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2  ")


def check_rows(row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2]) and board[row][0] != " "


def check_cols(col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col]) and board[0][col] != " "


def check_diagonals():
    one = (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[1][1] != " "
    two = (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[1][1] != " "
    res = one or two
    return res


def main():
    player = "X"

    for _ in range(9):
        # Change turn
        print_board()

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

        # check winner
        winner = False

        for i in range(3):
            if check_rows(i):
                winner = player
                break
            if check_cols(i):
                winner = player
                break
            if check_diagonals():
                winner = player

        if winner:
            print_board()
            print(f"Congratulations! Player {player} wins!")
            break

    else:
        print_board()
        print("We have draw!")


# main
main()
