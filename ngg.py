#!/usr/bin/python3
# Number Guessing Game
# Created by Nicholas Lueth, 8/24/2021 

# Import randint to get random number
from random import randint

# Game object
class Game:
    # Object initialization
    def __init__(self):
        # Random number the user is trying to guess is between 1 and 100
        self.number = randint(1, 100)
        # The number of tries it takes the user to guess the number
        self.tries = 0
        # The high end guess by the user
        self.highend = 100
        # The low end guess by the user
        self.lowend = 1

    # This function plays the game
    def play(self):
        # The guess startes out of guessing range, this is to assign the variable
        guess = -1
        # Loop until the user guesses the number
        while guess != self.number:
            # Make sure that the user types an integer
            try:
                guess = int(input(f"Guess the number {self.lowend}-{self.highend}: "))
            except ValueError:
                print("Your guess must be a number!")
            else:
                # If the guess is out of range of the high and low end variables, have the user guess again
                if self.lowend > guess  or guess > self.highend:
                    print("Guess out of range, try again.\n")
                    continue
                # If the guess is in range increment the number of tries
                self.tries += 1
                # If the user gets the answer right on the first try, offer to play again
                if guess == self.number and self.tries == 1:
                    print(f"You win! The number was {self.number}\nIt took you {self.tries} try! Did you cheat?\n")
                    self.play_again()
                # If the user guesses the number, offer to play again
                elif guess == self.number and self.tries != 1:
                    print(f"You win! The number was {self.number}\nIt took you {self.tries} tries!\n")
                    self.play_again()
                # If the guess is lower than the number adjust the low end number
                elif guess < self.number:
                    print(f"The number is higher than {guess}\n")
                    if guess > self.lowend:
                        self.lowend = guess
                # If the guess is higher than the number adjust the high end number
                elif guess > self.number:
                    print(f"The number is lower than {guess}\n")
                    if guess < self.highend:
                        self.highend = guess

    # This function prompts the user if they'd like to play again
    def play_again(self):
        # Repeat the question until the user gives a valid response
        while True:
            play_again = input("Would you like to play again y/n?").lower()
            # If the user types "y", reset the game and play again
            if play_again == "y":
                self.reset()
                # Adds an empty line between the old game and the new one
                print()
                self.play()
            # If the user types "n", quit
            elif play_again == "n":
                exit(0)
            # If the user types something else, inform them that they need to reply in the correct format
            else:
                print("Incorrect format, please type either y for yes, or n for no, to play again.\n")

    # This function resets the values in the game
    def reset(self):
        self.number = randint(1, 100)
        self.tries = 0
        self.highend = 100
        self.lowend = 1

# Creates the inital game object
mygame = Game()
# Start playing the game
mygame.play()
