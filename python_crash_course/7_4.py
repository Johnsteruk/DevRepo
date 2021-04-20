#!/usr/bin/env python3

#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
#pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.

active = True
while active:
    topping = input("Enter your pizza topping: ")
    
    if topping == 'quit':
        active = False
    else:
        print(f'...adding {topping}')

#7-5. Movie Tickets: A movie theater charges different ticket prices depending on
#a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#$15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket.
active = True
while active:
    age = input("Please input the users age: ")
    if age == 'quit':
        active = False
    else:    
        age = int(age)
        if age < 3 :
            print("No charge")
        elif age >= 3 and age <= 12:
            print("Price = $10")
        else:
            print("Price = $15")

    

#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
#that do each of the following at least once:
#• Use a conditional test in the while statement to stop the loop.
#• Use an active variable to control how long the loop runs.
#• Use a break statement to exit the loop when the user enters a 'quit' value.


#7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
#ctrl -C or close the window displaying the output.