#!/usr/bin/env python3
myName = input("Hello, what is your first name? : ")
myName = myName.title()

if myName == 'Carla':
    print("Wow, are you the famous Carla Whittaker?")
print(f"{myName} is a really nice name.")
age = input(f"\nHow old are you {myName}? : ")
print(f"Well {age} is not REALLY old.")
lives = input(f"\nWhere do you live {myName} : ")
livesDuration = input(f"How many years have you lived in {lives} {myName}? : ")
print(f"\nWow! have you really lived in {lives} for {livesDuration} years? That is a long time {myName}.")
haircolour = input("\nWhat colour is your hair? : ")
print(f"You have {haircolour} hair. That is really cool {myName}!")
print(f"The people in {lives} will really love your {haircolour} hair.")
walks = input("\nDo you like going for long walks? (yes or no): ")
if walks.lower() == 'yes':
    print('Good, walking is good exercise.')
else:
    print('That is a shame, because walking is good exercise.')

favBand = input(f"\nWhat is the name of your favourite band? : ")
print(f"If {favBand.title()} are ever playing near {lives} you should try to go to see them.")
ipad = input("\nDo you have an ipad? (yes or no) : ")
if ipad.lower() == 'yes':
    game = input("Good. What games do you like to play? : ")
    print(f"\n{game.title()} is a good game to play.")

game = input("\nDo you want to play a game (yes or no) : ")
if game.lower() == 'yes':
    from random import randrange
    secretNumber = randrange(1,11)

    guesscount = 0
    guess = 11

    print('I am thinking of a number between one and 10. Can you guess what it is?')

    while guess != secretNumber:   
        guess = input('\nGuess a number between 1 and 10 : ')
        guess = int(guess)
        guesscount += 1
        if guess == secretNumber:
            if guesscount == 1:
                print(f"\nWell done, you guessed the number in {guesscount} try! AWESOME! The number was {secretNumber}.")
            else:
                print(f"\nWell done, you guessed the number in {guesscount} tries! The number was {secretNumber}.")
        elif guess < secretNumber:
            print("You have guessed too low. Try again.")
        elif guess > secretNumber:
            print("You have guessed too high. Try again.")


nextAge = int(age) +1

print(f"\nIt has been nice speaking to you {myName}. \nI hope to see you and your {haircolour} hair again soon. \nHappy birthday when you turn {nextAge}")



