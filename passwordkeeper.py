# Author: Jack Randall
# Date: 5/13/24
# Description: a program that stores passwords and usernames of websites you input and gives you various options of what to do with them
# Bugs: N/A
# Challenges: makes the user enter a password to access the program, allow the user to change specific usernames and passwords, allow the user to retroactively add more usernames and passwords

websites = ["Google"]                                                       #makes websites equal a list of websites you can add to with one preset website
usernames = ["googledoodle@gmail.com"]                                      #makes usernames equal a list of usernames you can add to with a parallel username to the preset website
passwords = ["sundar_pichai55"]                                             #makes passwords equal a list of passwords you can add to with a parallel username to the preset website

import time                                                                 #creates the ability to implement time into the program

def loading():                                                              #creates a function that replicates loading
    '''
    Simulates loading after the user inputted the main password.

    Args:
        None.
    
    Prints:
        Each loading position consecutively to make it seem like the program is loading.
    '''
    for i in range(4):                                                      #for each number that makes up 4
        print("loading" + "."*i)                                            #print loading plus the amount of dots that mirror the index the program is currently at
        time.sleep(0.9)                                                     #wait 0.9 seconds to print the next thing
def secure_word():                                                          #creates a function that makes a password to access the program
    '''
    Creates a secure password to get into the main program.
    
    Args:
        None.
    
    Prints:
        Says welcome if they enter the right password, and if they enter the wrong one, it informs them that it is the wrong password.
    
    Functions:
        If the user enters the right password, it lets them into the program, if they enter the wrong one, it exits the program.
    '''
    secure_password = input("What is the password? ")                       #asks the user to input the password
    if secure_password == "jrandall_24":                                    #if the users input is the correct password
        loading()                                                           #run the loading function
        print("Welcome!")                                                   #let the user into the program
        print()                                                             #create a space
    else:                                                                   #if the users input is not the correct password
        loading()                                                           #run the loading function
        print("That is not the password, access denied!")                   #tell the user that is not the password
        exit()                                                              #end the program

def main():                                                                 #creates a main function that runs the actual program and contains all of the code
    secure_word()                                                           #run the security function
    while True:                                                             #creates a infinite while true loop
        choice = str.upper(input('''What will you do?
    A. Enter info
    B. Print info
    C. Access specific username and password 
    D. Change a username and password
    E. End the program
Your choice: '''))                                                          #choice asks the user which action they will choose and automatically makes the users response uppercase
        print()                                                             #create a space
        if choice == "E":                                                   #if the users input is E
            print("Come again soon!")                                       #notify the user that the program has ended by saying come again soon
            break                                                           #end the while true loop and the program
        elif choice == "A":                                                 #if the users input is A
            websites.append(input("What is your website? "))                #let the user input their website name and add the users corresponding input to the websites list
            usernames.append(input("What is your username? ") )             #let the user input their username and add the users corresponding input to the usernames list
            passwords.append(input("What is your password? "))              #let the user input their password and add the users corresponding input to the passwords list
            print()                                                         #create a space
        elif choice == "B":                                                 #if the users input is B
            for i in range(len(websites)):                                  #for each index of the length of websites
                print(f'''Website #{i+1}: {websites[i]}
Username #{i+1}: {usernames[i]}
Password #{i+1}: {passwords[i]}''')                                         #print the website number and corresponding website, the username number and corresponding username, and the password number and corresponding password
                print()                                                     #create a space
        elif choice == "C":                                                                             #if the users input is C
            website_choice = input("Which website's username/password do you want to access? ")         #let the user input which website's username and password they want to see
            if website_choice in websites:                                                              #if their choice is in the websites list
                i = websites.index(website_choice)                                                      #defines i as equaling the index of the users choice in websites
                print(f'''Username: {usernames[i]}
Password: {passwords[i]}''')                                                                            #print the specific username and password                                             
                print()                                                                                 #create a space
            else:                                                                                       #if the users input isn't in the websites list
                print("We do not see that website in our database")                                     #inform the user that the website is not in the database
                print()                                                                                 #create a space
        elif choice == "D":                                                                             #if the users input is D
            website_change = input("Which website's username/password would you like to replace? ")     #let the user input what website that has the username and password they want to change
            if website_change in websites:                                                              #if the users input is in the websites list
                i = websites.index(website_change)                                                      #defines i as equaling the index of the users choice in websites
                usernames[i] = input("Change username: ")                                               #let the user input the new username and replace the old on in the usernames list
                passwords[i] = input("Change password: ")                                               #let the user input the new password and replace the old on in the passwords list
                print()                                                                                 #create a space
            else:                                                                                       #if the users input isn't in the websites list
                print("We do not see that website in our database")                                     #inform the user that the website is not in the database
                print()                                                                                 #create a space
        else:                                                                                           #if the users main input is not A, B, C, D, or E
            print("Please enter either A, B, C, D, or E")                                               #inform the user that they have to input again
            print()                                                                                     #create a space

main()                                                                                                  #run the main function