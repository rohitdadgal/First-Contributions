def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins! Congratulations!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()