board = {'1': " ", '2': " ", '3': " ", '4': " ", '5': " ", '6': " ", '7': " ", '8': " ", '9': " "}


# Gives idea to player for where to enter the values
def instruction_board():
    print("     |     |     ")
    print("  1  |  2  |  3  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  4  |  5  |  6  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  7  |  8  |  9  ")
    print("     |     |     ")

# Initiate the game
def start_playing():
    print('\n\n Welcome!! Start Playing Tic Tac Toe!!!! \n\n')
    print("Please enter the positions as mentioned below")
    instruction_board()

# Reset the board values to start the game again
def reset_board():
    for key in board.keys():
        board[key] = " "


# gameByPlayerX = False
# gameByPlayerO = False

# Returns all the keys in a list
def return_actual_list():
    board_keys_list = []
    for val in board.keys():
        board_keys_list.append(val)
    return board_keys_list

# This will print the board with the updated values from the list
def print_board():
    print("     |     |     ")
    print(f"  " + board['1'] + "  |  " + board['2'] + "  |  " + board['3'] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  " + board['4'] + "  |  " + board['5'] + "  |  " + board['6'] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  " + board['7'] + "  |  " + board['8'] + "  |  " + board['9'] + "  ")
    print("     |     |     ")

# Winner decider method, premutations of possible winning chances
def winner():
    if board['1'] == board['2'] == board['3'] == 'X' or board['4'] == board['5'] == board['6'] == 'X' or board[
        '7'] == board['8'] == board['9'] == 'X' or board['1'] == board['4'] == board['7'] == 'X' or board['2'] == \
            board['5'] == board['8'] == 'X' or board['3'] == board['6'] == board['9'] == 'X' or board['1'] == \
            board['5'] == board['9'] == 'X' or board['3'] == board['5'] == board['7'] == 'X':
        winner_status = True
        return winner_status
    elif board['1'] == board['2'] == board['3'] == 'O' or board['4'] == board['5'] == board['6'] == 'O' or board[
        '7'] == board['8'] == board['9'] == 'O' or board['1'] == board['4'] == board['7'] == 'O' or board['2'] == \
            board['5'] == board['8'] == 'O' or board['3'] == board['6'] == board['9'] == 'O' or board['1'] == \
            board['5'] == board['9'] == 'O' or board['3'] == board['5'] == board['7'] == 'O':
        winner_status = True
        return winner_status
    else:
        winner_status = False
        return winner_status

# Updates the value on the board
def update_board_value(key, value):
    board[key] = value

# Update the board dictionary with the values to be placed in the position
def check_value_in_list(result, value, positionList):
    if result not in return_actual_list():
        print("Invalid value selected!! please select a value from 1 to 10")
        return False
    elif result not in positionList:
        positionList.append(result)
        update_board_value(result, value)
        print_board()
        return True
    else:
        print("Value already selected!! Please enter another value")
        return False

# Get the input from the user to place X or O
def ask_for_value(i, positionList):
    if winner() == False:
        if i % 2 == 0:
            value = 'X'
            result = input(f"Select a position you wish to enter '{value}' : \n")
        else:
            value = 'O'
            result = input(f"Select a position you wish to enter '{value}' :\n")
        return check_value_in_list(result, value, positionList)

# Decides the chance of player
def chance_of_player():
    reset_board()
    positionList = []
    i = 0
    player1 = input("\nPlayer 1 please select either 'X' or 'O' \n")
    while " " in board.values() and winner() != True and positionList != return_actual_list():
        if player1 in ['X', 'x']:
            j = ask_for_value(i, positionList)
        elif player1 in ['O', 'o']:
            j = ask_for_value(i + 1, positionList)
        else:
            print("Invalid input provided !!!!!!")
            break
        if j == True:
            i = i + 1
    final_check()

# Gives user an option to play again
def final_check():
    # if winner() and player1.lower() == 'x' and gameByPlayerX:
    #     print("Player 1 is the Winner")
    # elif winner() and player1.lower() == 'o' and gameByPlayerO:
    #     print("Player 1 is the Winner")
    # elif winner() and player1.lower() != 'x' and gameByPlayerO:
    #     print("Player 2 is the Winner")
    # elif winner() and player1.lower() != 'o' and gameByPlayerX:
    #     print("Player 2 is the Winner")
    if winner():
        print("\nCongratulations you won the game !!! \n")
    else:
        print("\nNo Winner!! \n")

    print(("Would you like to try again !!!!"))
    play_again = input("Please enter Yes/No : \n")
    if play_again.lower() == 'yes':
        chance_of_player()
    elif play_again.lower() == 'no':
        print("Thanks for playing!!! Come Again :)")
    else:
        print("Invalid input provided!!!")


# Entry point to the game

start_playing()
chance_of_player()
