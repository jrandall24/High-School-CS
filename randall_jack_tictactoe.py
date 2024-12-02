'''
Name: Jack Randall
Description: A program that lets the user play tictactoe against another user on the same device or a computer that chooses random positions
Log: v1.0, initial version
Bugs: Returns an error if inputting a spot that has already been played as the last move, then inputting the last available spot, returns a draw when playing another user and inputting a spot that has already been played as the last move
Features: None
Sources: W3Schools, GeeksforGeeks
'''

#imports random which gives the program the ability to choose something random out of a list and imports time to let the program wait
import random
import time

#creates a list consisting of 'X' and 'O'
x_or_o = ['X', 'O']
#creates an array to be the tictactoe board
board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
def print_tictactoe():
    '''
    Prints the tictactoe board efficiently

    Returns:
        int: the numbers within the list with three numbers per row in ascending order from 1-9
    '''
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='  ')
        print()
def user(player, move):
    '''
    Goes through each spot on the board and checks if the user's input is one of the spots. If the user's input is an available spot on the board, put their symbol in the spot that was inputted, and if not, tell the user to try again

    Args:
        input: the player's move
        str: the user's assigned symbol (X or O)
    Returns:
        str: the user's symbol in the spot that they inputted on the array
    Raises:
        inputError: return skip into the main function when the user's input is not on the board
    '''
    if board[0][0] == 1 and move == '1':
        board[0][0] = player
    elif board[0][1] == 2 and move == '2':
        board[0][1] = player
    elif board[0][2] == 3 and move == '3':
        board[0][2] = player
    elif board[1][0] == 4 and move == '4':
        board[1][0] = player
    elif board[1][1] == 5 and move == '5':
        board[1][1] = player
    elif board[1][2] == 6 and move == '6':
        board[1][2] = player
    elif board[2][0] == 7 and move == '7':
        board[2][0] = player
    elif board[2][1] == 8 and move == '8':
        board[2][1] = player
    elif board[2][2] == 9 and move == '9':
        board[2][2] = player
    else:
        return 'skip'
def check_win(player):
    '''
    Checks if the possible winning combinations are on the board and says which player (X or O) wins

    Args:
        input: the player's move
    Returns:
        str: informing the user(s) which one wins
        function: exits the program
    '''
    if board[0][0] == board[1][1] == board[2][2]:
        print(player, 'wins!')
        exit()
    elif board[0][2] == board[1][1] == board[2][0]:
        print(player, 'wins!')
        exit()
    elif board[0][0] == board[1][0] == board[2][0]:
        print(player, 'wins!')
        exit()
    elif board[0][1] == board[1][1] == board[2][1]:
        print(player, 'wins!')
        exit()
    elif board[0][2] == board[1][2] == board[2][2]:
        print(player, 'wins!')
        exit()
    elif board[0][0] == board[0][1] == board[0][2]:
        print(player, 'wins!')
        exit()
    elif board[1][0] == board[1][1] == board[1][2]:
        print(player, 'wins!')
        exit()
    elif board[2][0] == board[2][1] == board[2][2]:
        print(player, 'wins!')
        exit()
def main():
    '''
    Asks the user whether they'd like to play a bot or a player, then repeatedly asks the user(s) for their input and runs the check_win and user functions, additionally showing the tictactoe board after every input

    Returns:
        array: runs the print_tictactoe function after every input
    Raises:
        inputError: when the user does not input U or C when asked whether to play another user (U) or a computer (C)
        inputError: when the user does not input F or S when asked whether they want to go first (F) or second (S) when playing a computer
        inputError: if the user does not input a spot on the board when asked, return skip
    '''
    #asks the user whether they want to play a user or computer, if they input anything but U or C, make them input again
    while True:
        user_or_cpu = str.upper(input('If you would like to play a user, type U, if you would like to play a computer, type C: '))
        if user_or_cpu == 'U':
            break
        elif user_or_cpu == 'C':
            break
        else:
            print('Incorrect input, please try again')
    #if the user selects U, assign X and O, and create a loop that asks the user whos turn it is for their input, shows the board, and checks whether a user wins or they draw
    if user_or_cpu == 'U':
        user1 = random.choice(x_or_o)
        x_or_o.remove(user1)
        user2 = x_or_o[0]
        print('Assigning X and O...')
        time.sleep(1.5)
        print(f'''
User 1: {user1}
User 2: {user2}

User 1 goes first
''')
        print_tictactoe()
        move_loop = 0
        can_move = ''
        while move_loop < 9:
            if can_move != 'skip':
                choice = input(f'User 1 ({user1}): Where would you like to move? Please enter a number on the board: ')
                can_move = user(user1, choice)
                print_tictactoe()
                check_win(user1)
                move_loop += 1
            else:
                print('That spot has already been played or your input is not on the board, please try again')
                can_move = ''
                move_loop -= 1

            if move_loop >= 9:
                print('Draw!')
                exit()

            if can_move != 'skip':
                choice = input(f'User 2 ({user2}): Where would you like to move? Please enter a number on the board: ')
                can_move = user(user2, choice)
                print_tictactoe()
                check_win(user2)
                move_loop += 1
            else:
                print('That spot has already been played or your input is not on the board, please try again')
                can_move = ''
                move_loop -= 1
    #if the user inputs C, ask the user whether they'd like to go first or second, and if they don't input F or S, make them input again
    if user_or_cpu == 'C':
        while True:
            user_turn = str.upper(input('If you would like to go first, type F, if you would like to go second, type S: '))
            if user_turn == 'F':
                break
            elif user_turn == 'S':
                break
            else:
                print('Incorrect input, please try again')
        #if the user chose to go first, assign X and O, then make a loop that asks the user where they'd like to go, show the board, and make the computer choose a random spot to go
        if user_turn == 'F':
            user1 = x_or_o[0]
            computer = x_or_o[1]
            print('User goes first')
            move_loop = 0
            can_move = ''
            print_tictactoe()
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            while move_loop < 9:
                if can_move != 'skip':
                    choice = input('User: Where would you like to move? Please enter a number on the board: ')
                    can_move = user(user1, choice)
                    print_tictactoe()
                    check_win(user1)
                    if choice in numbers:
                        numbers.remove(choice)
                    else:
                        continue
                    move_loop += 1

                if move_loop >= 9:
                    print('Draw!')
                    exit()

                if can_move != 'skip':
                    print('Computer moving...')
                    time.sleep(1.5)
                    bot_move = random.choice(numbers)
                    can_move = user(computer, bot_move)
                    print_tictactoe()
                    check_win(computer)
                    if bot_move in numbers:
                        numbers.remove(bot_move)
                    else:
                        continue
                    move_loop += 1
                else:
                    print('That spot has already been played or your input is not on the board, please try again')
                    can_move = ''
                    move_loop -= 1
        #if the user chose to go first, assign X and O, then make a loop that makes the computer choose they're spot, show the board, then ask the user where they'd like to go
        elif user_turn == 'S':
            user1 = x_or_o[1]
            computer = x_or_o[0]
            print('Computer goes first')
            move_loop = 0
            can_move = ''
            print_tictactoe()
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            while move_loop < 9:
                if can_move != 'skip':
                    print('Computer moving...')
                    time.sleep(1.5)
                    bot_move = random.choice(numbers)
                    can_move = user(computer, bot_move)
                    print_tictactoe()
                    check_win(computer)
                    if bot_move in numbers:
                        numbers.remove(bot_move)
                    else:
                        continue
                    move_loop += 1
                else:
                    print('That spot has already been played or your input is not on the board, please try again')
                    can_move = ''
                    move_loop -= 1
                
                if move_loop >= 9:
                    print('Draw!')
                    exit()

                if can_move != 'skip':
                    choice = input('User: Where would you like to move? Please enter a number on the board: ')
                    can_move = user(user1, choice)
                    print_tictactoe()
                    check_win(user1)
                    if choice in numbers:
                        numbers.remove(choice)
                    else:
                        continue
                    move_loop += 1
main()
