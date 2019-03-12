#Jacob Shoup Final Project
#Roll a Dice


# Imports the necessary modules
import random

dice = input("How many dice do you want to roll? ")
# Sets the roll variable as true
roll = True

# Added "while' loop to ask for later use input
while roll:
    print("rolling dice...")
    for i in range (dice):
        print("You rolled", random.randit(1, 6)))
    roll = input("Do you want to roll again? (yes or no): ")
# Prints a number between 1 and 6 and asks if the user wants to roll again
    if roll == "yes":
        continue
    else:
        break







