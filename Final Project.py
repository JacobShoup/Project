#Jacob Shoup Final Project
#Roll a Dice


# Imports the necessary modules
import random


# Sets the roll variable as true
roll = True

# Added "while' loop to ask for later use input
while roll:
    print("rolling dice...")
    print("you rolled", random.randint(1, 6))
    roll = input("Do you want to roll again? (yes or no): ")
# Prints a number between 1 and 6 and asks if the user wants to roll again
    if roll == "yes":
        continue
    else:
        break







