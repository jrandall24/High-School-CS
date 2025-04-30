'''
Name: Jack Randall
Description: lets the user play a game of battleship against a computer opponent
Date: 5/1/25
Log: v1.0, initial version
Bugs: N/A
Features: emojis, lets the user place their ships, computer has turns
Sources: none
Tester: Oliver Servedio
'''
import random
import os
import time
#creates four boards for the players ships, computers ships, user's guesses, and an empty board for confirming inputs
player_ships = [
        	['A1', 'B1', 'C1', 'D1', 'E1'],
            ['A2', 'B2', 'C2', 'D2', 'E2'],
            ['A3', 'B3', 'C3', 'D3', 'E3'],
            ['A4', 'B4', 'C4', 'D4', 'E4'],
            ['A5', 'B5', 'C5', 'D5', 'E5'],
          ]
bot_ships = [
        	['A1', 'B1', 'C1', 'D1', 'E1'],
            ['A2', 'B2', 'C2', 'D2', 'E2'],
            ['A3', 'B3', 'C3', 'D3', 'E3'],
            ['A4', 'B4', 'C4', 'D4', 'E4'],
            ['A5', 'B5', 'C5', 'D5', 'E5'],
          ]
guesses = [
        	['A1', 'B1', 'C1', 'D1', 'E1'],
            ['A2', 'B2', 'C2', 'D2', 'E2'],
            ['A3', 'B3', 'C3', 'D3', 'E3'],
            ['A4', 'B4', 'C4', 'D4', 'E4'],
            ['A5', 'B5', 'C5', 'D5', 'E5'],
          ]
empty_board = [
        	['A1', 'B1', 'C1', 'D1', 'E1'],
            ['A2', 'B2', 'C2', 'D2', 'E2'],
            ['A3', 'B3', 'C3', 'D3', 'E3'],
            ['A4', 'B4', 'C4', 'D4', 'E4'],
            ['A5', 'B5', 'C5', 'D5', 'E5'],
          ]
def print_ships(board):
    '''
    Prints the battleship board efficiently

    Returns:
        str: the board to be printed
    Args: 
        none
    '''
    for i in range(len(board)):             #for each row in the board
        for j in range(len(board[i])):      #for each column in the row
            print(board[i][j], end=' ')     #print the value at that position in the board
        print()
def player_placement():
    '''
    Places the user's ships on the board. The user has five ships to place

    Returns:
        func: the print_ships function to print the board
        str: if placement is not available, the user is prompted to try again
    Args:
        none
    '''
    ships = 0
    while ships < 5:
        print_ships(player_ships)
        count = 0
        placement = input('Place battleship: ').upper()
        for y in range(len(player_ships)):                                              #for each row in the board
            for x in range(len(player_ships)):                                          #for each column in the row
                if player_ships[y][x] == placement and player_ships[y][x] != '🛥️ ':     #if the coordinate equals the input and the coordinate does not already have a ship
                        player_ships[y][x] = '🛥️ '                                      #replace the coordinate with a ship
                        ships += 1
                        count += 1
        if count < 1:
            print('Position is not available')
def computer_placement():
    '''
    Places the computer's ships on the board. The computer has five ships to place

    Returns:
        none
    Args:
        none
    '''
    ships = 0
    while ships < 5:
        count = 0
        #randomly generates a row and column for the computer to place its ship
        row = random.randrange(len(bot_ships))
        col = random.randrange(len(bot_ships[row]))
        #the computer's choice is the coordinate at the randomly generated row and column
        placement = bot_ships[row][col]
        for y in range(len(bot_ships)):                                         #for each row in the board
            for x in range(len(bot_ships)):                                     #for each column in the row
                if bot_ships[y][x] == placement and bot_ships[y][x] != '🛥️ ':   #if the coordinate equals the random input and the coordinate does not already have a ship
                    bot_ships[y][x] = '🛥️ '                                     #replace the coordinate with a ship
                    ships += 1
                    count += 1
        if count < 1:
            continue
def player_guess():
    '''	
    The user guesses where the computer's ships are located. The function checks if the guess is correct and updates the board accordingly

    Returns:
        str: the board is updated with a hit (💥) if the guess is correct, or a miss (💢) if the guess is incorrect
        str: if the guess is incorrect, the user is prompted to try again
    Args:
        none
    '''
    while True:
        count = 0
        print('Your guesses:')
        print_ships(guesses)
        guess = input('Place your guess: ').upper()
        for y in range(len(bot_ships)):                #for each row in the board
            for x in range(len(bot_ships)):            #for each column in the row
                #if the coordinate already has a ship, the coordinate is the user's guess, and the coordinate does not already have a hit
                if bot_ships[y][x] == '🛥️ ' and empty_board[y][x] == guess and guesses[y][x] != '💥':
                    count += 1   #count is incremented by 1
                #if the coordinate does not have a ship, the coordinate is the user's guess, and the coordinate has not already been guessed
                elif bot_ships[y][x] != '🛥️ ' and guesses[y][x] != '💥' and guesses[y][x] != '💢' and empty_board[y][x] == guess:
                    count += 2   #count is incremented by 2
        #if the count is less than 1 due to the input not existing, the user is prompted to try again
        if count < 1:
            print('That input has already been guessed or is incorrect, please try again')
            continue
        #if the count is equal to 1, the guess is correct and the board is updated with a hit
        elif count == 1:
            print('User: HIT!')
            for y in range(len(guesses)):
                for x in range(len(guesses)):
                    if guesses[y][x] == guess:
                        guesses[y][x] = '💥'
            break
        #if the count is greater than 1, the guess is incorrect and the board is updated with a miss
        elif count > 1:
            print('User: MISS!')
            for y in range(len(guesses)):
                for x in range(len(guesses)):
                    if guesses[y][x] == guess:
                        guesses[y][x] = '💢'
            break
def bot_guess():
    '''
    The computer guesses where the user's ships are located. The function checks if the guess is correct and updates the board accordingly

    Returns:
        str: the board is updated with a hit (💥) if the guess is correct, or a miss (💢) if the guess is incorrect
        str: if the guess is incorrect, the user is prompted to try again
    Args:
        none
    '''
    while True:
        #randomly generates a row and column for the computer to guess
        row = random.randrange(len(player_ships))
        col = random.randrange(len(player_ships[row]))
        #the computer's guess is the coordinate at the randomly generated row and column
        guess = player_ships[row][col]
        #if the coordinate already been guessed, the computer guesses again
        if guess in ['💥', '💢']:
            continue 
        #if the coordinate on the user's board has a ship, the guess is correct and the board is updated with a hit
        if guess == '🛥️ ':
            print('Computer: HIT!')
            player_ships[row][col] = '💥'
            break
        #if the coordinate on the user's board does not have a ship, the guess is incorrect and the board is updated with a miss
        else:
            print('Computer: MISS!')
            player_ships[row][col] = '💢'
            break
def check_win(board, player):
    '''
    Checks if the computer or user (depending on who it is checking) has won by checking if all ships of their opponent have been hit

    Returns:
        str: if the player has won, the game ends
    Args:
        board: the board to be checked
        player: the user or computer
    '''
    count = 0
    for y in range(len(board)):         #for each row in the board
        for x in range(len(board)):     #for each column in the row
            if board[y][x] == '💥':     #if the coordinate has a hit
                count += 1              #add one to count
    #if there are 5 hits, the player has won
    if count == 5:
        print(player, 'wins!')
        exit()
def main():
    print('Place your battleships. You have five, so choose your spaces wisely! (🛥️  indicates a battleship)')
    player_placement()
    computer_placement()
    #clears the terminal
    os.system('cls')
    print('Time to play! 💥 indicates a hit and 💢 indicates a miss. Good luck!')
    while True:
        player_guess()
        player = 'User'
        check_win(guesses, player)          #runs the check win function for the user
        time.sleep(.5)
        bot_guess()
        player = 'Computer'
        check_win(player_ships, player)     #runs the check win function for the computer
        time.sleep(.5)
        print('Your ships:')
        print_ships(player_ships)
main()