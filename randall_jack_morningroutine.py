# Author: Jack Randall
# Date: 11/10/23
# Description: Makes a morning routine that includes different inputs whether the user responds with a yes or no answer.
# Bugs: N/A
# Challenges: While true statements loop the statement if the user answers with anything else but yes or no. Converts any user responses to lowercase.

print ("ALARM!") # Prints ALARM! and starts a string of questions

while True: # Creates a while true loop
    too_tired = str.lower(input("Are you too tired to get up? ")) # Asks the user if they are too tired to get up

    if too_tired == "no": # If the user answers with no, respond with you get up
        print ("You get up")
        break
    elif too_tired == "yes": # If the user answers with yes, respond with snooze and repeat the loop asking if you are too tired to get up

        while True:
            print ("Snooze")
            print ("ALARM!")
            too_tired = str.lower(input("Are you too tired to get up? "))
            if too_tired == "yes": # If the user answers yes again, repeat the loop
                continue
            elif too_tired == "no": # If the user answers with no, break the loop and print you get up
                print ("You get up")
                break
            else:
                print ("I won't accept that answer") # If the user answers with anything but yes or no, print I won’t accept that answer and loop it again
                continue
        break
    else: # If the user answers with anything but yes or no, print I won’t accept that answer and loop it again
        print ("I won't accept that answer")
        print ("Snooze")
        print ("ALARM!")
        continue

shower = str.lower(input("Shower? ")) # Create an input asking the user if they want to shower

if shower == "yes": # If the user answers yes, print you shower, now go get dressed and continue
    print ("You shower, now go get dressed")
    
elif shower == "no": # If the user answers no, it prints a statement and continues
    print ("You stink! Go get dressed stinky")

else: # If the user answers with anything else but yes or no, print a statement and continue
    print ("Stop entering gibberish, it's yes or no answers! You don't deserve a shower!")
    print ("Now go get dressed")

eat = str.lower(input("Eat? ")) # Creates an input and asks the user if they want to eat

if eat == "yes": # If the user answers with yes, print the statement and continue
    print("You eat, very yummy")

elif eat == "no": # If the user answers no, print the statement underneath and continue
    print("You'll be hungry")

else: # If the user answers with anything else but yes or no, print a statement and continue
    print("From now on, random things will equal yes")

print("Now get ready to leave")

get_ready = str.lower(input("Is it raining? ")) # Creates an input asking the user if its raining

if get_ready == "no": # If the user answers no, print get going to school and continue
    print("Get going to school")

else: # If the user answers with anything else but no, print the statement and continue
    print("Bring an umbrella and get going to school")

bus = str.lower(input("Take the bus? ")) # Create an input that asks the user if they want to take the bus

if bus == "no": # If the user answers with no, print you walk to school and continue
    print("You walk to school")
    
else: # If the user answers with anything else but no, print you have a nice bus ride and continue
    print("You have a nice bus ride")

print("Have a good day!") # Says have a good day and the code ends
