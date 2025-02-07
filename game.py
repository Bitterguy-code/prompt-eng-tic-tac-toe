import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} * {board[1]} * {board[2]}")
    print("- * - * -")
    print(f"{board[3]} * {board[4]} * {board[5]}")
    print("- * - * -")
    print(f"{board[6]} * {board[7]} * {board[8]}")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for cell in board)

# Minimax algorithm for AI decision-making
def minimax(board, depth, is_maximizing, player, ai):
    if check_winner(board, ai):
        return 1
    elif check_winner(board, player):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                score = minimax(board, depth + 1, False, player, ai)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(board, depth + 1, True, player, ai)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function for the AI to make the best move
def ai_move(board, player, ai):
    best_score = -float("inf")
    best_move = None

    # Find the best move using minimax
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = minimax(board, 0, False, player, ai)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    # If no best move is found (shouldn't happen), choose the first available move
    if best_move is None:
        for i in range(9):
            if board[i] == " ":
                best_move = i
                break

    # Make the move
    board[best_move] = ai

# Main game loop
def play_game():
    while True:
        # Initialize the board with empty spaces
        board = [" " for _ in range(9)]
        display_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])  # Show numbered board for reference

        # Ask the player to choose X or O
        player = input("Do you want to be X or O? ").upper()
        while player not in ["X", "O"]:
            player = input("Invalid choice. Please choose X or O: ").upper()

        ai = "O" if player == "X" else "X"
        print(f"You are {player}, and the AI is {ai}.")

        # Determine who goes first
        current_player = player if random.choice([True, False]) else ai
        print(f"{current_player} goes first!")

        # Game loop
        while True:
            if current_player == player:
                # Player's turn
                try:
                    move = int(input(f"Player {player}, enter a number (1-9) to make your move: ")) - 1
                    if move < 0 or move > 8 or board[move] != " ":
                        print("Invalid move. Try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue
                board[move] = player
            else:
                # AI's turn
                print("AI is making a move...")
                ai_move(board, player, ai)

            # Display the updated board
            display_board(board)

            # Check for a winner or a tie
            if check_winner(board, current_player):
                print(f"{current_player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            # Switch players
            current_player = player if current_player == ai else ai

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()