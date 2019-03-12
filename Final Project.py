#Jacob Shoup Final Project
#Roll a Dice


# Imports the necessary modules
import random

dice = int(input("How many dice do you want to roll? "))
sides = int(input("How many sides do you want the dice to have? ")
roll = True
# Sets the roll variable as true

# Added "while' loop to ask for later use input
while roll:
    print("rolling dice...")
    for i in range (dice):
        print("You rolled", random.randit(1, sides))
    roll = input("Do you want to roll again? (yes or no): ")
# Prints a number between 1 and 6 and asks if the user wants to roll again
    if roll == "yes":
        dice = int(input("How many dice do you want to roll? "))
        sides = int(input("How many sides do you want the dice to have? ")
        continue
    else:
        break

