#Author: Jack Randall
#Date: 5/31/24
#Description: Creates two pie charts consisting of the top 15 words used in the kamala_new file and the cleaned_trump_speech_transcript file
#Bugs: N/A
#Challenges: Used matplotlib instead of excel to create the pie chart

#imports a collection of useful constants and functions for working with strings and imports the library matplotlib and numpy
import string
import matplotlib.pyplot as plt
import numpy as np

#opens the kamala_new file as kamala, opens the cleaned_trump_speech_transcript file as trump, and opens the election_output file as new_file and lets it be written into
kamala = open('CS2\\kamala_new.txt')
trump = open('CS2\\cleaned_trump_speech_transcript.txt')
new_file = open('CS2\\election_output.txt', 'w')

def dictionary(fhand, new_file):
    '''
    Creates a dictionary taking in the words from the trump file and kamala file, imprting the top 15 most used words from each dictionary into new_file

    Args: 
        file: the kamala and trump speeches
    Returns:
        str: words from the kamala and trump speeches
        int: the amount of times the word shows up in the dictionary
        file: places data into the election_output file
    '''
    #creates dictionary for the file taken in by the function
    speech_dict = dict()
    #for every line in the file, get rid of spaces, punctuation, make everything lowercase, and make each word its own line
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        #for each word in the file, if the word hasn't been read by the function, make it's number of occurences 1, and if it has been read, add one to it's occurences
        for word in words:
            if word not in speech_dict:
                speech_dict[word] = 1
            else:
                speech_dict[word] += 1
    sorted_speech = dict(sorted(speech_dict.items(), key=lambda items: -items[1])) #sorts the list of words going from most occurences to least
    limit = 0                                                                      #makes the loop of words equal 0
    #for the first 15 words in the now sorted speech, add each word to new_file
    for key in sorted_speech:
        if limit < 15:
            final = key + ' ' + str(sorted_speech[key])
            new_file.write(final)
            new_file.write('\n')
            limit += 1
    new_file.write
#run the dictionary function with the kamala text and trump text while using the election_output as the file to import the code into
dictionary(kamala, new_file)
dictionary(trump, new_file)
new_file.close()                                  #close the election_output file

new_file = open('CS2\\election_output.txt', 'r')  #open the election_output file to read it

#the lists needed for kamala values, kamala words, trump values, and trump words to be implemented into the pit chart
kamala_values = []
kamala_words = []
trump_values = []
trump_words = []

amount = 0 #makes the loop of words equal 0
for line in new_file:
    #if the amount of words is less than 15, seperate each word, add each word to the kamala_words list, add each value to the kamala_value list, and add 1 to the loop
    if amount < 15:
        words = line.split()
        kamala_words.append(words[0])
        kamala_values.append(int(words[1]))
        amount += 1
    #if the amount of words is less than 30, seperate each word, add each word to the trump_words list, add each value to the trump_value list, and add 1 to the loop
    elif amount < 30:
        words = line.split()
        trump_words.append(words[0])
        trump_values.append(int(words[1]))
        amount += 1

chart = np.array(kamala_values)         #make the variable chart equal a numpy array for kamala_values
plt.pie(chart, labels = kamala_words)   #make a pie chart consisting of the kamala_values list and make each value's label it's corresponding word
plt.title('Kamala Data')                #make the pie chart's title 'Kamala Data'
plt.show()                              #show the kamala pie chart

chart = np.array(trump_values)          #make the variable chart equal a numpy array for trump_values
plt.pie(chart, labels = trump_words)    #make a pie chart consisting of the trump_values list and make each value's label it's corresponding word
plt.title('Trump Data')                 #make the pie chart's title 'Trump Data'
plt.show()                              #show the trump pie chart