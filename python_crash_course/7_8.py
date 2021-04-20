#!/usr/bin/env python3

#7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
#ous sandwiches. Then make an empty list called finished_sandwiches . Loop
#through the list of sandwich orders and print a message for each order, such
#as I made your tuna sandwich. As each sandwich is made, move it to the list
#of finished sandwiches. After all the sandwiches have been made, print a
#message listing each sandwich that was made.

sandwich_orders = []

sandwich_orders.append('egg')
sandwich_orders.append('ham')
sandwich_orders.append('chicken')
sandwich_orders.append('sausage')
sandwich_orders.append('tuna')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"currently making ... {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print(sandwich_orders)
print(finished_sandwiches)


#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
#the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has
#run out of pastrami, and then use a while loop to remove all occurrences of
#'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
#in finished_sandwiches .
sandwich_orders = ['cheese','beans','egg','pastrami', 'chicken', 'pastrami', 'ham','sausage','tuna','pastrami']
finished_sandwiches = []
print("We are sorry we have no more pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"currently making ... {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

#7-10. Dream Vacation: Write a program that polls users about their dream vaca-
#tion. Write a prompt similar to If you could visit one place in the world, where
#would you go? Include a block of code that prints the results of the poll.
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")

