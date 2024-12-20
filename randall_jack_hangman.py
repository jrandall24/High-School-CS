#Name: Jack Randall
#Description: A program that lets the user play hangman against the computer's list of words or another user's choice
#Log: v1.0, initial version
#Bugs: N/A
#Features: Give the user the ability to play one player or two player, clears terminal for two player
#Sources: W3Schools

#import a way to interact with the operating system, give the system a way to randomly pick something out of a list
import os                   
import random
#create the hangman visuals
hangman = ['''              
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
#function to check whether someone has won by checking whether _ are no longer in the hidden word
def check_win(one_or_two):
    if one_or_two == 'C':
        if '_' not in blank_word:
            print('You win! The word was', ''.join(word))
            exit()
    elif one_or_two == 'P':
        if '_' not in blank_word:
            print('Player 2 wins! The word was', ''.join(word))
            exit()
#repeatedly ask whether the user wants to play the computer or another player, repeat until the user inputs a correct input
while True:
    one_or_two = str.upper(input('Would you like to play a computer or another player? Type C for computer and P for player: '))
    if one_or_two == 'C':
        one_or_two.upper
        break
    elif one_or_two == 'P':
        one_or_two.upper
        break
    else:
        print('Incorrect input, please input C or P')
#if the user chooses to play the computer
if one_or_two == 'C':
    #takes in a file of a list of words, read the file, split into individual words, take a random choice from the file
    with open('CS2\\hangman_words.txt', 'r') as file:
        content = file.read()
        words_list = (content.split(' '))
    word = random.choice(words_list).upper()
#if the user chooses to play another user
elif one_or_two == 'P':
    #repeatedly ask player 1 to input a word to guess and make it uppercase, if the word isn't letters, make them input again
    while True:
        word_input = input('Player 1, please input a word: ')
        word = word_input.upper()
        if word.isalpha() == True:
            break
        else:
            print('That input is incorrect, please input one word made up of only letters')
    #clear the terminal
    os.system('cls')
#turn the word into blank spaces, start a list of guesses, make a list of all the letters in the alphabet, make the user's lives equal 6
blank_word = list('_' * len(word))
list_of_guesses = 'Previous Guesses: '
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lives = 6
while lives > 0:
    #run the check win function, print the hangman visual based on the user's lives, print the blank word
    check_win(one_or_two)
    print(hangman[-lives - 1])
    print('Word:', ''.join(blank_word), 'Lives left:',lives)
    #set up an input asking for the user's guess and make their guess uppercase
    guess = str.upper(input('Guess a letter: '))
    #if the user's guess is in the alphabet list
    if guess in alphabet:
        #if the user's guess is in the chosen word, make the variable that contained the checked location index equal zero, then check each letter in the word and add the letter to the right spot in the blank word
        if guess in word:
            same_letter = 0
            for i in word:
                same_letter += 1
                if guess == i:
                    blank_word[same_letter - 1] = guess
        #if the user's guess is not in the chosen word, deduct a life from the user
        else:
            print('Not here!')
            lives -= 1
        #add the user's guess to the list of guesses, print the list of guesses, then remove the user's guess from the alphabet list
        list_of_guesses = list_of_guesses + guess + ' '
        print(list_of_guesses)
        alphabet.remove(guess)
    #if the user guesses something not in the alphabet or a letter that has been removed from the alphabet list by being guessed previously, ask the user for a real input
    else:
        print('Incorrect input, please input one letter that has not been guessed before')
        print(list_of_guesses)
#if blank spots still remain in the hidden word after the user loses all of their lives = they lose
if '_' in blank_word:
    print(hangman[-lives - 1])
    print('You ran out of lives! Player 1 wins! The word was', ''.join(word))
#if blank spots don't remain in the hidden word after the user loses all of their lives, run the check_win function
else:
    check_win(one_or_two)
