# Author: Jack Randall
# Date: 12/1/23
# Description: A program that gives the user the ability to play rock paper scissors against a computer
# Bugs: N/A
# Challenges: Keeps score over multiple games, introduces a score limit, multiple different user errors addressed, addresses user error by printing a randomly selected message

import random # gives the program the ability to choose something random for a variety of different functions

user_p = 0 # sets the user points to 0
comp_p = 0 # sets the computer points to 0

plays = ["rock", "paper", "scissors"] # creates a list containing rock, paper, and scissors, the possible options for playing the game

print("Games are best of 7") # displays the message “Games are best of 7”

while True: # creates a while true loop and runs until broken
    user_rps = str.lower(input("Rock, paper, scissors says...? (enter stop to end) ")) # creates an input asking the user to input either rock, paper, scissors, or stop

    if user_rps == "stop": # if the user’s response is stop, then do something
        print("Let's play later") # displays the message “Let’s play later”
        break # stop the loop and end the code
    elif user_rps in plays: # if the user's response is in the plays list         print("Shoot!") # display the message “Shoot!”
        computer_rps = random.choice(plays) # set the variable computer_rps equal to choosing a random choice from the plays list
        print(computer_rps) # displays a random choice from the list to show if the computer chose rock, paper, or scissors

        if computer_rps == user_rps: # if the computer’s response is equal to the user’s response             
             print("You tie") # displays the message “You tie”
        elif computer_rps == "rock" and user_rps == "paper": # if the computer’s response is rock and the user’s response is paper then do something
            print("You win!") # displays the message “You win!”
            user_p += 1 # add one to the user’s points
        elif computer_rps == "paper" and user_rps == "rock": # if the computer’s response is paper and the user’s response is rock
            print("You lose") # displays the message “You lose”
            comp_p += 1 #add one to the computer’s points
        elif computer_rps == "scissors" and user_rps == "rock": # if the computer’s response is scissors and the user’s response is rock
            print("You win!") # displays the message “You win!”
            user_p += 1 # add one to the user’s points
        elif computer_rps == "rock" and user_rps == "scissors": # if the computer’s response is rock and the user’s response is scissors
            print("You lose") # displays the message “You lose”
            comp_p += 1 # add one to the computer’s points
        elif computer_rps == "paper" and user_rps == "scissors": # if the computer’s response is paper and the user’s response is scissors
            print("You win!") # displays the message “You win!”
            user_p += 1 # add one to the user’s points
        elif computer_rps == "scissors" and user_rps == "paper": # if the computer’s response is scissors and the user’s response is paper
            print("You lose") # displays the message “You lose”
            comp_p += 1 # add one to the computer’s points

        print(f"user wins: {user_p}") # after the round, display the user’s current points
        print(f"computer wins: {comp_p}") # after the round, display the computer’s current points

        if user_p == 4: # if the user’s points equals 4, do something
            print("You won the series!") # displays the message “You won the series!”
            user_p = 0 # set the user’s points to zero
            comp_p = 0 # set the computer’s points to zero
            continue # continue the loop
        elif comp_p == 4: # if the computer’s points equals 4, do something
            print("You lost the series") # displays the message “You lost the series”
            user_p = 0 # set the user’s points to zero
            comp_p = 0 # set the computer’s points to zero
            continue # continue the loop
    else: # if the user inputs anything else besides rock, paper, or scissors, do something
        print(random.choice(["You have to enter rock, paper, scissors", "You gotta enter rock, paper, or scissors, take this seriously", "Invalid response, that makes no sense to me", "Rock, paper, or scissors?", "You gonna pick your weapon or not?"])) # displays a random choice from a list of responses that print when the user inputs something besides rock, paper, or scissors


