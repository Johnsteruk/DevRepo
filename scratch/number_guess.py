#!/usr/bin/env python3

from random import randrange
secretNumber = randrange(1,11)

guesscount = 0
guess = 11

while guess != secretNumber:
    guess = input('Guess a number between 1 and 10 : ')
    guess = int(guess)
    guesscount += 1
    if guess == secretNumber:
        if guesscount == 1:
            print(f"\nWell done, you guessed the number in {guesscount} try! AWESOME!")
        else:
            print(f"\nWell done, you guessed the number in {guesscount} tries!")
    elif guess < secretNumber:
        print("You have guessed too low. Try again.")
    elif guess > secretNumber:
        print("You have guessed too high. Try again.")




#game = input("Do you want to play a game? (yes or no) : ")
#if game.lower() == 'yes':
