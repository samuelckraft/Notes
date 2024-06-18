#PIP stands for "Pip Installs Packages" or "Pip installs python"
#Command line tool that helps install, update and remove python packages

#Random package
import random

for _ in range(10): #10 is number of times rolled
    dice_roll = random.randint(1,6) #(1,6) is the potential values of the dice rolls
    print("You rolled a " + str(dice_roll) + "!")


import random

playlist = ['Kendrick', 'J Cole', 'Lil Wayne', 'Eminem', 'Juice']

random.shuffle(playlist)

for x in playlist:
    print(x)
    

#randomized loop
import random

snacks = ['apple', 'yogurt', 'smoothie', 'eggs', 'chocolate bar']
picked_snack = ''

while picked_snack != 'chocolate bar':
    picked_snack = random.choice(snacks)
    print("You are eating a " + picked_snack)
    if picked_snack != 'chocolate bar':
        print("Let's get another")
    else:
        print("Oh yum chocolate my favorite")