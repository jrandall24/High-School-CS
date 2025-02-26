'''
Name: Jack Randall
Description: A program that takes the user's input and lets them choose from a selection of string functions
Log: v1.0, initial version
Bugs: N/A
Features: Functions menu, bonus functions
Sources: letter subtotals(https://stackoverflow.com/questions/5664494/letter-count-dictionary), how to use ordinals(https://initialcommit.com/blog/python-ord-function)
'''
import random
#1
def reverse(word):
    '''
    Description: Reverse string inputted by the user
    
    Args:
        str: user's name/word
    Returns:
        str: user's input reversed
    '''
    final_word = []
    word_list = list(word)
    #takes each letter in the word and puts it in the first position of the final_word list, pushes every other letter back one
    for letter in word_list:
        final_word.insert(0, letter)
    return ''.join(final_word)
#2
def vowel_check(word):
    '''
    Description: Returns the subtotals of each vowel in the user's input
    
    Args:
        str: the user's input
    Returns:
        dict: each vowel in the word with their corresponding number of times they appeared
    '''
    word = make_lower(word)
    vowels = list('aeiouy')
    counts = dict()
    word_list = list(word)
    #for each letter in the word, if the letter is a vowel, set its count to 0 and then add 1
    for letter in word_list:
        if letter in vowels:
            counts[letter] = counts.get(letter, 0) + 1
        else:
            continue
    #return the letters with their corresponding values
    return counts
#3
def consonant_check(word):
    '''
    Description: Returns the subtotals of each consonant in the user's input
    
    Args:
        str: the user's input
    Returns:
        dict: each consonant in the word with their corresponding number of times they appeared
    '''
    word = make_lower(word)
    consonants = ('bcdfghjklmnpqrstvwxz')
    counts = dict()
    word_list = list(word)
    #for each letter in the word, if the letter is a consonant, set its count to 0 and then add 1
    for letter in word_list:
        if letter in consonants:
            counts[letter] = counts.get(letter, 0) + 1
        else:
            continue
    #return the letters with their corresponding values
    return counts
#4
def first_name(word):
    '''
    Description: Returns the first name of the user's input
    
    Args:
        str: the user's input
    Returns:
        str: the first name
    '''
    name_list = word.split(' ')
    titles = ['Mr.', 'Ms.', 'Mrs.', 'Miss', 'Rev.', 'Gen.', 'Lt.', 'Dr.', 'Sir', 'Esq.', 'Ph.D']
    #for each name in the titles list if the title is in the user's input, remove it
    for name in titles:
        if name in name_list:
            name_list.remove(name)
    #return first name
    return name_list[0]
#5
def last_name(word):
    '''
    Description: Returns the last name of the user's input
    
    Args:
        str: the user's input
    Returns:
        str: the last name
    '''
    name_list = word.split(' ')
    titles = ['Mr.', 'Ms.', 'Mrs.', 'Miss', 'Rev.', 'Gen.', 'Lt.', 'Dr.', 'Sir', 'Esq.', 'Ph.D']
    #for each name in the titles list if the title is in the user's input, remove it
    for name in titles:
        if name in name_list:
            name_list.remove(name)
    #return the last name
    return name_list[-1]
#6
def middle_name(word):
    '''
    Description: Returns the middle name(s) of the user's input
    
    Args:
        str: the user's input
    Returns:
        str: the middle name(s)
        str: no middle name detected if there isn't any middle names in the user's input
    '''
    name_list = word.split(' ')
    titles = ['Mr.', 'Ms.', 'Mrs.', 'Miss', 'Rev.', 'Gen.', 'Lt.', 'Dr.', 'Sir', 'Esq.', 'Ph.D']
    #if the length of the split input is greater than two, for each name in the titles list if the title is in the user's input, remove it
    if len(name_list) > 2:
        for name in titles:
            if name in name_list:
                name_list.remove(name)
        #remove the first and last names, then return the middle names
        name_list.pop(0), name_list.pop(-1)
        return ' '.join(name_list)
    #if the split input only has two objects, detect no middle name
    else: return 'No middle name detected'
#7
def hyphen_check(word):
    '''
    Description: Checks if the last name inputted by the user contains a hyphen
    
    Args:
        str: the user's input
    Returns:
        boolean: true or false depending on if the last name has a hyphen
    '''
    name_list = word.split(' ')
    #check each letter in the last name, and if there is a hyphen, return true, if there isn't, return false
    for i in name_list[-1]:
        if i == '-':
            return True
    return False
#8
def make_lower(word):
    '''
    Description: Makes the user's input lowercase
    
    Args:
        str: the user's input
    Returns:
        str: the lowercase output
    '''
    lower_word = []
    for letter in word:
        #check if the ordinal of the letter is between 65 and 90 (uppercase), and if it is, add 32 to its ordinal, making it lowercase
        if ord(letter) >= 65 and ord(letter) <= 90:
            lower_word.append(chr(ord(letter)+32))
        else:
            #if the ordinal is not uppercase, leave it be
            lower_word.append(letter)
    #return the lowercase output
    return ''.join(lower_word)
#9
def make_upper(word):
    '''
    Description: Makes the user's input uppercase
    
    Args:
        str: the user's input
    Returns:
        str: the uppercase output
    '''
    upper_word = []
    for letter in word:
        #check if the ordinal of the letter is between 97 and 122 (lowercase), and if it is, subtract 32 from its ordinal, making it uppercase
        if ord(letter) >= 97 and ord(letter) <= 122:
            upper_word.append(chr(ord(letter)-32))
        else:
            #if the ordinal is not uppercase, leave it be
            upper_word.append(letter)
    #return the lowercase output
    return ''.join(upper_word)
#10
def mix_letters(word):
    '''
    Description: Randomly mixes up the letters of the user's input
    
    Args:
        str: the user's input
    Returns:
        str: the mixed up output
    '''
    word_list = list(word)
    scramble = []
    #while there are still letters in the word list, add a random letter to a new list and remove that letter from the old list
    while len(word_list) > 0:
        random_letter = random.choice(word_list)
        scramble.append(random_letter)
        word_list.remove(random_letter)
    #return the mixed up output
    return ''.join(scramble)
#11
def palindrome(word):
    '''
    Description: Checks if the first name is a palindrome
    
    Args:
        str: the user's input
    Returns:
        boolean: true or false depending on whether the first name is a palindrome
    '''
    final_name = []
    #runs the function that takes the first name of the input and turns the first name into a list
    name_list = list(first_name(word))
    #reverse the indexes of each letter in the first name
    for letter in name_list:
        final_name.insert(0, letter)
    #if the original name and reversed name are the same, return true, if they're different, return false
    if make_lower(final_name) == make_lower(name_list):
        return True
    else:
        return False
#12
def sort_name(word):
    '''
    Description: Sorts the user's input
    
    Args:
        str: the user's input
    Returns:
        str: the sorted output
    '''
    #turns the name into a list, sorts each character, and returns it
    name_list = list(word)
    name_list.sort()
    return ''.join(name_list)
#14
def initials(word):
    '''
    Description: Takes the initials of each input separated by spaces in the user's input
    
    Args:
        str: the user's input
    Returns:
        str: the uppercase output
    '''
    word_list = word.split(' ')
    initials = []
    #for each index in the split input, if the name is not a title, add the name's first letter to the initials list
    for i in word_list:
        if i not in ['Mr.', 'Ms.', 'Mrs.', 'Miss', 'Rev.', 'Gen.', 'Lt.', 'Dr.', 'Sir', 'Esq.', 'Ph.D']:
            initials.append(list(i)[0])
    #return the initials
    return ''.join(make_upper(initials))
#15
def have_title(word):
    '''
    Description: Check's if the user's input has a title in the title list
    
    Args:
        str: the user's input
    Returns:
        boolean: true or false depending on whether the user's input contains a title
    '''
    titles = ['Mr.', 'Ms.', 'Mrs.', 'Miss', 'Rev.', 'Gen.', 'Lt.', 'Dr.', 'Sir', 'Esq.', 'Ph.D']
    #check each name in the user's input, if there is a title return true, if there isn't return false
    for name in word.split(' '):
        if name in titles:
            return True
    return False
#16
def cipher(word):
    '''
    Description: Replace the user's input with symbols in a parallel list
    
    Args:
        str: the user's input
    Returns:
        str: the encrypted input
        str: not encryptable if the function cannot encrypt the input
    '''
    #parallel encryption and alphabet lists
    encryption = list('!@&^(#*%)_-|[X};/><~=+Q`P,Z')
    alphabet = list('abcdefghijklmnopqrstuvwxyz ')
    encrypted_word = []
    #for every letter in the word, if the letter is in the alphabet list, add the symbol with the parallel index to that letter to the new word
    for letter in list(word):
        if letter in alphabet:
            encrypted_word.append(encryption[alphabet.index(letter)])
        #if a part of the input is not in the alphabet list, return not encryptable
        else:
            return 'Not encryptable'
    #return the encrypted word if encryptable
    return ''.join(encrypted_word)
#17
def decipher(word):
    '''
    Description: Returns the user's encrypted word back to normal
    
    Args:
        str: the user's encrypted word
    Returns:
        str: the normal word
        str: not decryptable if the function cannot decrypt the input
    '''
    #parallel encryption and alphabet lists
    encryption = list('!@&^(#*%)_-|[X};/><~=+Q`P,Z')
    alphabet = list('abcdefghijklmnopqrstuvwxyz ')
    decrypted_word = []
    #for every letter in the word, if the letter is in the encryption list, add the letter with the parallel index to that letter to the new word
    for letter in list(word):
        if letter in encryption:
            decrypted_word.append(alphabet[encryption.index(letter)])
        #if a part of the input is not in the encryption list, return not decryptable
        else:
            return 'Not decryptable'
    #return the encrypted word if decryptable
    return ''.join(decrypted_word)
#13
def main():
    #ask the user for their input
    word_input = input('Input your word/name to use: ')
    word_or_name = word_input
    while True:
        #the menu for the user to reference
        print(f'''
Original input = {word_input}
Functions:
1. Reverse and display
2. Determine the number of vowels
3. Consonant frequency
4. Give first name
5. Give last name
6. Give middle name(s)
7. Return boolean if last name contains a hyphen
8. Convert to lowercase
9. Convert to uppercase
10. Modify array to create a random name (mix up letters)
11. Return boolean if first name is a palindrome
12. Return full-name as a sorted array of characters
13. Take initials from name
14. Return boolean if name contains a title/distinction (Mr., Ms., Mrs., Miss, Rev., Gen., Lt., Dr., Sir, Esq., Ph.D)
15. Encrypt an input
16. Decrypt an input
17. Exit 
----''')
        #ask the user for which function they want to run, then run the function they choose, printing the output from the function, if the function they input doesn't exist, don't run anything and restart the while True
        func_choice = input('Which function would you like to run? (input the functions number): ')
        if func_choice == '1':
            print('Reversed word:', reverse(word_or_name))
        elif func_choice == '2':
            print('Vowel numbers:', vowel_check(word_or_name))
        elif func_choice == '3':
            print('Consonant numbers:', consonant_check(word_or_name))
        elif func_choice == '4':
            print('First name:', first_name(word_or_name))
        elif func_choice == '5':
            print('Last name:', last_name(word_or_name))
        elif func_choice == '6':
            print('Middle name(s):', middle_name(word_or_name))
        elif func_choice == '7':
            print('Hyphen check:', hyphen_check(word_or_name))
        elif func_choice == '8':
            print('Lowercase output:', make_lower(word_or_name))
        elif func_choice == '9':
            print('Uppercase output:', make_upper(word_or_name))
        elif func_choice == '10':
            print('Random name:', mix_letters(word_or_name))
        elif func_choice == '11':
            print('Palindrome check:', palindrome(word_or_name))
        elif func_choice == '12':
            print('Sorted name:', sort_name(word_or_name))
        elif func_choice == '13':
            print('Initials:', initials(word_or_name))
        elif func_choice == '14':
            print('Title check:', have_title(word_or_name))
        elif func_choice == '15':
            print('Encryption:', cipher(word_or_name))
        elif func_choice == '16':
            print('Decryption:', decipher(word_or_name))
        elif func_choice == '17':
            print('Goodbye!')
            exit()
        else:
            print('Please input a functions number')
            continue
main()