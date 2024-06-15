# Function to initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check for a tie
def check_tie(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to validate a move
def is_valid_move(board, row, col):
    return board[row][col] == ' '
# Minimax function with optional Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    # Check for terminal states
    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1  # Human wins
    elif check_tie(board):
        return 0  # Tie

    if is_maximizing:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if is_valid_move(board, row, col):
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if is_valid_move(board, row, col):
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval
# Function to determine the best move for the AI
def best_move(board):
    best_value = -float('inf')
    move = None
    for row in range(3):
        for col in range(3):
            if is_valid_move(board, row, col):
                board[row][col] = 'O'
                move_value = minimax(board, 0, False)
                board[row][col] = ' '
                if move_value > best_value:
                    best_value = move_value
                    move = (row, col)
    return move


# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe! You are X and AI is O.")
    print_board(board)

    while True:
        # Human move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if is_valid_move(board, row, col):
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                print_board(board)
                print("You win!")
                break
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                break
        else:
            print("Invalid move. Try again.")
            continue

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
            if check_winner(board, 'O'):
                print_board(board)
                print("AI wins!")
                break
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

        print_board(board)


if __name__ == "__main__":
    play_game()
