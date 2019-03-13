# Jacob Shoup
# Final Project
# Roll a Dice

# Imports the needed module
import random
import time

# Asks the user how many dice they want to roll, how many sides the dice should have,
# and what to do with the values
def roll_dice(x):
    dice = int(input("How many dice do you want to roll? "))
    sides = int(input("How many sides do you want the dice to have? "))
    sum = input("Do you want to add your dice together? (yes or no): ")
    average = input("Do you want to average your dice roll? (yes or no): ")
    roll = True

# Chooses a random number within the users specified range and calculates the Sum and
# average if the user asked for it
    while roll:
        amount = 0
        print("rolling dice...")
        for i in range (dice):
            time.sleep(x)
            number = random.randint(1, sides)
            print("You rolled", number)
            amount = amount + number
        if sum == "yes":
            print("Sum: ", amount)
        if average == "yes":
            sumav = amount/(float(dice))
            print("Average: ", sumav)

# Asks the user if they want to roll again and restarts the program if they do
        roll = input("Do you want to roll again? (yes or no): ")
        if roll == "yes":
            dice = int(input("How many dice do you want to roll? "))
            sides = int(input("How many sides do you want the dice to have? "))
            sum = input("Do you want to add your dice together? (yes or no): ")
            average = input("Do you want to average your dice roll? (yes or no): ")
            continue
        else:
            break

        print("Thank you for rolling the dice")

# Runs the program
roll_dice(1)
