import os


board = [" " for _ in range(9)]  # positions 0-8, empty string board

# Map positions to a 3x3 grid visually (0,1,2 / 3,4,5 / 6,7,8) — this makes win-checking with index math much easier than nested lists.

# Functions to write

# display_board(board) — prints the board using | and rows

def display_board(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("---  ---  ---")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("---  ---  ---")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("---  ---  ---")
# get_move(player) — asks for input (1-9 is more human-friendly than 0-8), validates it's a valid number and the spot isn't taken
def get_move(player):

    move = int(input(f"Player{player} please enter your move between 1 and 9: "))
    valid = False
    while not valid:
        if 1 <= move <= 9:
            global board
            if board[move-1] == " ":
                valid = True
            else:
                print("Move was invalid spot was already taken.")
                move = int(input(f"{player} please enter your move between 1 and 9 "))
        else:
            print("Move was invalid only a whole number between 1 and 9 inclusive")
            move = int(input(f"{player} please enter your move between 1 and 9 "))


    return move-1
# check_win(board, player) — checks all 8 win combinations (3 rows, 3 cols, 2 diagonals)
def check_win(board, player_symbol):
    for combo in win_combos:
        if board[combo[0]] == player_symbol and board[combo[1]] == player_symbol and board[combo[2]] == player_symbol:
            return True

    return False
# check_draw(board) — checks if board is full with no winner
def check_draw(board):
    for i in range(9):
        if board[i] == " ":
            return False
    return True

# play_game() — main loop: alternate turns, display board, check win/draw after each move
def play_game():
    result = False
    player_symbols =  ["X","O"]
    player_moves = [[],[]]
    win = False
    draw = False
    while not result:

        for player in range(2):

            player += 1
            move = get_move(player)
            if player == 1:
                player_moves[player-1].append(move)
                board[move] = player_symbols[player-1]
            else:
                player_moves[player-1].append(move)
                board[move] = player_symbols[player-1]
            display_board(board)
            if check_draw(board) or check_win(board,player_symbols[player-1]):
                result = True
                if check_win(board,player_symbols[player-1]):
                    win = True
                    win_player = player
                elif check_draw(board):
                    draw = True

                break
    display_board(board)
    if win:
        print(f"Player{win_player} won")
    elif draw:
        print("Its a draw")


# Win-checking trick: hardcode the winning index combos as a list of tuples:
win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

if __name__ == "__main__":

    print("Welcome to tic tac toe")

    continue_ = True
    while continue_:
        play_game()
        os.system('cls' if os.name == 'nt' else 'clear')
        user_continue = input("Do you want to continue playing another game ?")

        if user_continue.upper() == "NO":
            continue_ = False





