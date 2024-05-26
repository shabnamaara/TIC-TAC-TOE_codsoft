def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row number (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column number (0, 1, 2): "))
        
        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue
        
        board[row][col] = player
        
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break
        
        player = "O" if player == "X" else "X"

tic_tac_toe()
