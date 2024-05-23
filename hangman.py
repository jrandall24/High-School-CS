import random

hangman_pics = ['''              
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

words = ["hello", "world", "python"]    # possible words to choose from for the player to guess
secret = random.choice(words)           # choose a secret word randomly from the list of possible words
secret_list = list(secret)              # convert the secret word into a list by splicing the characters
hidden = []                             # create an empty list to be used as a way for player to keep track of their guesses
guesses = 0                             # variable to keep track of how many incorrect guesses the player has made; starts at zero

# adds to the hidde list such that the characters in the secret list line up with the dashes to indicate the length etc of the word to the players
for character in secret_list:           # literate through every element (character) in the list of the secret word's characters
    if character == " ":                # if the character is a space
        hidden.append("  ")             # add two spaces to the hidden list to demonstrate that there are multiple words
    else:                               # otherwise
        hidden.append("_ ")             # add a dash and space to the hidden list to represent a character

print("".join(hidden))                  # converts the hidden list into a string, which is displayed, by joining each character in its list

while "_ " in hidden and guesses < len(hangman_pics) - 1:       #
    while True:
        guess = str.lower(input("Enter a letter: "))

        if guess not in list("abcdefghijklmnopqrstuvwxyz "):
            print("Please enter a letter!")
        else:
            break

    if guess in secret_list:
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print("".join(hidden))
    else:
        print("Not here!")
        guesses += 1
        print(hangman_pics[guesses])

if "_ " in hidden:
    print(f"You lost! The word was {secret}.")
else:
    print("You won!")


