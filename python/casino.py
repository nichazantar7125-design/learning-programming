# Import librates and packages
from random import randint
import os

# Declare and initialize variables and/or constants
player_lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0
dices_add = 0
status = True

# Functions
def roll_dices() :
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        return dice1, dice2

# Main
while status :
    os.system('cls')
    dices = roll_dices()
    roll_count+=1
    dices_add = 0
    print("#" * 20)
    print(f"Roll dices N°: {roll_count}")
    print("#" * 20)
    print(f"Player lives: {player_lives}")
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")
    dices_add = dices[0] + dices[1]

    if dices_add % 2 != 0:
        player_lives-=1
        print(f"You've lost one live ::: Now you have {player_lives} lives")
        if player_lives == 0:
            print("::: Game Over :::")
            break

    print(f"Dices addition: {dices_add}")

    if roll_count == 5:
        break
    else: 
        press_key = input("\nPress any key to roll dices again")