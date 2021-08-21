import random
import time

def roll_dice(count_dice):
    roll_values = []

    while True:
        start_roll = input("Press enter to roll the dice!")
        for i in range(count_dice):
            roll_values.append(random.randint(1, 6))
        print("\nRolling the dice...")
        time.sleep(1.3)
        if count_dice == 1:
            print("\nYou rolled a " + str(roll_values[0]) + "!")
        elif count_dice == 2:
            print("\nYou rolled a " + str(roll_values[0]) + ", and a " + str(roll_values[1]) + " for a total of " + str(sum(roll_values)) + "!")
        roll_values.clear()


print("Welcome to Dice-Roller!")

while True:
    try:
        count_dice = int(input("\nAre you looking for 1 or 2 dice? "))
        if count_dice == 1 or count_dice == 2:
            roll_dice(count_dice)
        else:
            print("\nSorry, please enter either 1 or 2.")
    except ValueError:
        print("\n Sorry, please enter either 1 or 2.")