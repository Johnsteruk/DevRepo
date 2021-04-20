#!/usr/bin/env python3

#7-1. Rental Car: Write a program that asks the user what kind of rental car they
#would like. Print a message about that car, such as “Let me see if I can find you
#a Subaru.”
car = input("Please enter the car you would like: ")
print(f"\nLets see if I can find you a, {car.title()}!")

#7-2. Restaurant Seating: Write a program that asks the user how many people
#are in their dinner group. If the answer is more than eight, print a message say-
#ing they’ll have to wait for a table. Otherwise, report that their table is ready.
numberOfPeople = input("Please enter the number of people to be seated : ")
numberOfPeople = int(numberOfPeople)

if numberOfPeople < 8:
    print(f"OK your table for {str(numberOfPeople)} is ready.")
else:
    print(f"You will have to wait for a table. {str(numberOfPeople)} is a big party!")


#7-3. Multiples of Ten: Ask the user for a number, and then report whether the
#number is a multiple of 10 or not.

myNum = input("Please enter a number : ")
myNum = int(myNum)

if myNum % 10 == 0:
    print(f"{str(myNum)} is divisible by 10!")
else:
    print(f"Not divisible by 10.")