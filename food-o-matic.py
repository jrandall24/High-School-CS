# Author: Jack Randall
# Date: 3/26/23
# Description: a program that generates an amount of different meals with various items for the user
# Bugs: N/A
# Challenges: creates a limit for how many meals the user can ask for, sets a price for each item and adds them up for total cost of each meal

import random #lets the program pick a random choice from a list 

main_courses = ["Cheeseburger", "Hot Dog", "Chili", "Cheesesteak", "Ceasar Salad", "Grilled Cheese", "BLT", "Lobster Tail", "Spicy Chicken Sandwich", "Chicken Legs"] #creates a list of different main courses
m_costs = [9.99, 5.50, 7.99, 10.99, 4.99, 3.50, 6.99, 16.99, 14.50, 12.99] #creates a list of parallel prices for each main course
sides = ["French Fries", "Tomato Soup", "Mac 'n' Cheese", "Mashed Potatos", "Sweet Potato Fries", "Cornbread", "Baked Beans", "Coleslaw", "Collard Greens", "Baked Potato"] #creates a list of different side dishes
s_costs = [3.99, 5.99, 4.50, 4.99, 3.50, 2.50, 4.50, 2.99, 3.50, 3.99] #creates a list of parallel prices for each side dish
drinks = ["Water", "Lemonade", "Coca Cola", "Fanta", "Dr. Pepper", "Beer", "Redbull", "Cocktail", "Orange Juice", "Milkshake"] #creates a list of different drinks
d_costs = [1.50, 2.50, 1.99, 1.99, 1.99, 4.50, 1.99, 5.50, 1.75, 3.99] #creates a list of parallel prices for each drink

while True: #creates an infinite loop
    number_of_meals = int(input("How many meals would you like? ")) #asks the user for the amount of meals they would like and makes the input have to be an  integer

    if number_of_meals <= 10: #if the number of dishes inputted by the user is less that or equal to ten
        for i in range(number_of_meals): #for the index of the number inputted by the user
            main_course = random.choice(main_courses) #establishes that main_course equals a random choice of items from the list of main courses
            side = random.choice(sides) #establishes that side equals a random choice of items from the list of sides
            drink = random.choice(drinks) #establishes that drink equals a random choice of items from the list of drinks
            print(f"{(main_course)}, {(side)}, {(drink)}. Cost: ${round(m_costs[main_courses.index(main_course)]+ s_costs[sides.index(side)]+ d_costs[drinks.index(drink)],2)}") #prints the main course, side, and drink chosen, and finds the index of the food or drink item and matches it with the corresponding price, adding each price up into a total price of the meal
        break #end the loop

    elif number_of_meals > 10: #if the number inputted by the user is greater than 10
        print("We apologize, but there isn't enough food in the kitchen for that amount, please try again") #print this statement


