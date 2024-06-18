#Task 1
username = str(input("What is your username? "))

if len(username) < 10:
    print('I\'m sorry that is not a valid username')
else:
    print(f"Welcome {username}")

print(' ')

#Task 2
prices = float(input("How much is the item? "))
rounded_price = round(prices, 2)

print(f"Rounded price: ${rounded_price}")

print(' ')
#Task 3
celsius_temps = [10, 25, 20, 30, 35]

for x in celsius_temps:
    farenheit_temps = (x * 9/5)+32
    print(f"{x}C is equivalent to {farenheit_temps}F")

print(' ')
#Task 4
room_temps = [70, 55, 67, 48, 80]
rooms = ['living room', 'kitchen', 'bedroom', 'bathroom', 'patio']

warmest = max(room_temps)
coldest = min(room_temps)


print(f"The warmest room is the {rooms[room_temps.index(warmest)]} at {warmest}F and the coldest room is the {rooms[room_temps.index(coldest)]} at {coldest}F")

print(' ')

#Task 5
product_1 = "milk"
product_2 = "eggs"
product_3 = "honey"

price_1 = "$5"
price_2 = "$3"
price_3 = "$9"

stock_1 = True
stock_2 = False
stock_3 = True

cart_summary = "In cart: \n"
cart_summary += "- " + product_1 + ": " + price_1 + (" (In Stock)" if stock_1 else " (Out of Stock)") + "\n"
cart_summary += "- " + product_2 + ": " + price_2 + (" (In Stock)" if stock_2 else " (Out of Stock)") + "\n"
cart_summary += "- " + product_3 + ": " + price_3 + (" (In Stock)" if stock_3 else " (Out of Stock)") + "\n"

print(cart_summary)

print(' ')

#Task 6
print("You wake up in a mysterious forest with two paths in front of you. Do you go left or right?")

choices = ['left', 'right']
outcomes = ['You encounter a friendly elf who offers you a map.', 'You stumble upon a sleeping dragon']

decision = input().lower()

if decision not in choices:
    print("You must be confused, you can only go left or right")
elif decision == 'left':
    outcome_index = choices.index('left')
    print(outcome_index)
    print(outcomes[outcome_index])
else:
    outcome_index = choices.index('right')
    print(outcomes[outcome_index])


print(' ')

#Task 7
shopping_list = ['apples', 'bananas', 'carrots', 'bread', 'milk']

seperator = input("Please enter your preferred item separator: ")
ending = input("Please enter your preffered ending phrase: ")

print("Your shopping list: ", end = "\n \n")
for x in shopping_list:
    if x == shopping_list[-1]:
        print(x)
    else:
        print(x, end=seperator + " ")
print("\n \n" + ending)

print(' ')

#Task 8
questions = [
    "What is 10+4",
    "Enter a decimal number between 1 and 2",
    "What is the string representation of the number 20",
    "Is python a programming language? (True/False)"
]

correct_answers = [14, 1.5, "20", True]
answer_types = [int, float, str, bool]

score = 0

for y in range(len(questions)):
    user_answer = input(questions[y] + " ")
    try:
        if answer_types[y] == bool:
            converted_answer = user_answer.lower() in ['true', 't', '1', 'yes', 'y']
        else:
            converted_answer = answer_types[y](user_answer)
        
        if converted_answer == correct_answers[y]:
            print("Correct")
            score += 1
        else:
            print("Wrong")
    except ValueError:
        print("Invalid input type")

print(f"Your final score is {score}/{len(questions)}")

print(' ')

#Task 9
mixed_list = [10, 3.14, 'Python', False, 42, 'Code', 2.718, True, 1]

integers = []
floats = []
strings = []
booleans = []

for z in mixed_list:
    if isinstance(z, int) and not isinstance(z, bool):
        integers.append(z)
    elif isinstance(z, float):
        floats.append(z)
    elif isinstance(z, str):
        strings.append(z)
    elif isinstance(z, bool):
        booleans.append(z)
    else:
        print(f"Unknown type: {type(z)}")

print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
print(f"Booleans: {booleans}")


print(" ")

#Task 10
import math

numbers = [2.5, 3.6, 4.7, 5.8, 6.9]

total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")

average = total_sum / len(numbers)
print(f"The average is: {average}")

for n in numbers:
    sqrt_number = math.sqrt(n)
    rounded_number = round(sqrt_number)
    if rounded_number < sqrt_number:
        rounded_number = math.ceil(sqrt_number)
    else:
        rounded_number = math.floor(sqrt_number)

    if rounded_number > average:
        print(f"{rounded_number} is above the average")
    else:
        print(f"{rounded_number} is below the average")