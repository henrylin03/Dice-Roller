import random, time

print("""Welcome! This app rolls dice for when you can't find them, but want to play. 

Let's get rollin'!
""")

no_of_dice = 0

while no_of_dice < 1:
    try:
        no_of_dice = int(input("How many dice do you need? "))
        if no_of_dice >= 1:
            min = no_of_dice # can also make it so that min and max are always 1 and 6 and then for loop when I roll based on how many they typed
            max = 6 * no_of_dice
        else:
            print("Sorry, please enter a whole number greater than or equal to 1")
    except ValueError:
        print("Sorry, please enter a whole number greater than or equal to 1")


while True:
    roll = input("Ready to roll? Y/N ")
    if roll == "Y" or roll == "Yes":
        print("Rolling the dices...")
        time.sleep(1)
        print("The total value is " + str(random.randint(min, max)))
    continue