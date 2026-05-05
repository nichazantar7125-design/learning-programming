from random import randint

# Functions
def roll_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

# Variables
status = True
count = 0
consecutive_pairs = 0

while status:
    input("Presiona ENTER para lanzar los dados...")  
    dices = roll_dices()
    count += 1
    print(f"Lanzamiento {count}: {dices}")
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")

    if (dices[0] == dices[1]):
        print("¡Par! You're win")
        consecutive_pairs += 1
        print(f"Pares seguidos: {consecutive_pairs}")

        if consecutive_pairs == 3:
            print("¡Ganaste definitivamente con tres pares seguidos!")
            status = False
        else:
            print("¡Sigue lanzando para intentar llegar a tres pares seguidos!")
    else:
        print("Try again !!!")
        consecutive_pairs = 0  

print(f"Total de lanzamientos: {count}")

