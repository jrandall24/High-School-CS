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
    #create a list of words, take a random choice from the list, turn the word into blank spaces, start a list of guesses, make a list of all the letters in the alphabet, make the user's lives equal 6
    words_list = ('able about account acid across addition adjustment advertisement after again against agreement almost among amount amusement angle angry animal answer apparatus apple approval arch argument army attack attempt attention attraction authority automatic awake baby back balance ball band base basin basket bath beautiful because before behaviour belief bell bent berry between bird birth bite bitter black blade blood blow blue board boat body boiling bone book boot bottle brain brake branch brass bread breath brick bridge bright broken brother brown brush bucket building bulb burn burst business butter button cake camera canvas card care carriage cart cause certain chain chalk chance change cheap cheese chemical chest chief chin church circle clean clear clock cloth cloud coal coat cold collar colour comb come comfort committee common company comparison competition complete complex condition connection conscious control cook copper copy cord cork cotton cough country cover crack credit crime cruel crush current curtain curve cushion damage danger dark daughter dead dear death debt decision deep degree delicate dependent design desire destruction detail development different digestion direction dirty discovery discussion disease disgust distance distribution division door doubt down drain drawer dress drink driving drop dust early earth east edge education effect elastic electric engine enough equal error even event ever every example exchange existence expansion experience expert face fact fall false family farm father fear feather feeble feeling female fertile fiction field fight finger fire first fish fixed flag flame flat flight floor flower fold food foolish foot force fork form forward fowl frame free frequent friend from front fruit full future garden general girl give glass glove goat gold good government grain grass great green grey grip group growth guide hair hammer hand hanging happy harbour hard harmony hate have head healthy hear hearing heart heat help high history hole hollow hook hope horn horse hospital hour house humour idea important impulse increase industry insect instrument insurance interest invention iron island jelly jewel join journey judge jump keep kettle kick kind kiss knee knife knot knowledge land language last late laugh lead leaf learning leather left letter level library lift light like limit line linen liquid list little living lock long look loose loss loud love machine make male manager mark market married mass match material meal measure meat medical meeting memory metal middle military milk mind mine minute mist mixed money monkey month moon morning mother motion mountain mouth move much muscle music nail name narrow nation natural near necessary neck need needle nerve news night noise normal north nose note number observation offer office only open operation opinion opposite orange order organization ornament other oven over owner page pain paint paper parallel parcel part past paste payment peace pencil person physical picture pipe place plane plant plate play please pleasure plough pocket point poison polish political poor porter position possible potato powder power present price print prison private probable process produce profit property prose protest public pull pump punishment purpose push quality question quick quiet quite rail rain range rate reaction reading ready reason receipt record regret regular relation religion representative request respect responsible rest reward rhythm rice right ring river road roll roof room root rough round rule safe sail salt same sand scale school science scissors screw seat second secret secretary seed seem selection self send sense separate serious servant shade shake shame sharp sheep shelf ship shirt shock shoe short shut side sign silk silver simple sister size skin skirt sleep slip slope slow small smash smell smile smoke smooth snake sneeze snow soap society sock soft solid some song sort sound soup south space spade special sponge spoon spring square stage stamp star start statement station steam steel stem step stick sticky stiff still stitch stocking stomach stone stop store story straight strange street stretch strong structure substance such sudden sugar suggestion summer support surprise sweet swim system table tail take talk tall taste teaching tendency test than that then theory there thick thin thing this thought thread throat through through thumb thunder ticket tight till time tired together tomorrow tongue tooth touch town trade train transport tray tree trick trouble trousers true turn twist umbrella under unit value verse very vessel view violent voice waiting walk wall warm wash waste watch water wave weather week weight well west wheel when where while whip whistle white wide will wind window wine wing winter wire wise with woman wood wool word work worm wound writing wrong year yellow yesterday young').split(' ')
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