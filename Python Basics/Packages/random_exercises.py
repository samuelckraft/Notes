#Task 1
import random #only need to put import random in once and you can import it on future equations

for _ in range(50):
    y = random.randint(1,10)
    if y == 3:
        print(f"Good job {y} was the number I was thinking of")
        break
    else:
        print(f"{y} isn't it, try again")

print(" ") 

#Task 2

directions = ['North', 'South', 'East', 'West']

for step in range(5):
    step_direction = random.choice(directions)
    print(f"Step {step + 1}: You move 10 steps to the {step_direction}")

print(' ')
#Task 3

#Their example
#while True:
#   dice1 = random.randomint(1,6)
#   dice2 = random.randomint(1,6)
#   print(f"Dice 1: {dice1}, Dice 2: {dice2})
#   if dice1 == dice2:
#       print(f"Both dice landed on {dice1})
#       break
for _ in range(1):
    lottery_numbers1 = random.randint(1,10)
    lottery_numbers2 = random.randint(1,10)
    lottery_numbers3 = random.randint(1,10)
    lottery_numbers4 = random.randint(1,10)
    lottery_numbers5 = random.randint(1,10)
    print(f"And the winning numbers are: {lottery_numbers1} - {lottery_numbers2} - {lottery_numbers3} - {lottery_numbers4} - {lottery_numbers5}")


print(" ")
#Task 4

#Their example
#questions = [1, 2, 3, 4] (not really but dont feel like typing them out)
#random.shuffle(questions)
#for x in questions:
#   print(x)
categories = ['Fiction', 'Sports', 'TV Shows', 'Geography', 'History']

picked_category = ''

while picked_category != 'TV Shows':
    picked_category = random.choice(categories)
    print(f"And the category is: {picked_category}")
    if picked_category == 'TV Shows':
        break

print(' ')
#Task 5
students = ['Mike', 'Jeff', 'Joe', 'John']

random.shuffle(students)

print(students)

print(" ")

#Task 6
#My attempt
#for _ in range(1):
#    character1 = random.randbytes(2)
#    print(character1)

import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(6))

print(f"Generated password: {password}")

print(" ")

#Task 7

num_colors = 1

for _ in range(num_colors):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    print(f"Generated RGB color: ({red}, {green}, {blue})")
