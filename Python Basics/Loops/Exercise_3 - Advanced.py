#Task 1
students = ['John', 'Jane', 'Jack', 'Jessica', 'Joseph']

top_students = students[:3]

for x in top_students:
    print(f"Congrats, {x} you are in the top of your class")

print(" ")

#Task 2
inventory = ['Apples', 120, 'Oranges', 80, True, 'Bananas', 150, False]

index = 0

while index < len(inventory):
    item = inventory[index]

    if type(item) == str:
        print(f"Item: {item}")
    elif type(item) == int:
        print(f"Quantity: {item}")
    elif type(item) == bool:
        status = "on sale" if item else "not on sale"
        print(f"Sale status: {status}")

    index += 1

print(" ")

#Task 3

squares = [number**2 for number in range(1,11)]

print(squares)

print(' ')

#Task 4
jersey_numbers = list(range(1,21))

even_numbers = [x for x in jersey_numbers if x % 2 == 0]

print(even_numbers)

print(' ')

#Task 5
ingredients = ['salt', 'pepper', 'paprika', 'garlic', 'onion', 'beef', 'tomato', 'basil']

needed_ingredients = ingredients[:len(ingredients)//2]

print(needed_ingredients)

print(' ')

#Task 6
articles = ["War", "Peace", "Finance", "Politics", "Sports"]


last_three = articles[-3:]

last_three.reverse()

print(last_three)

print(' ')

#Task 7
#Their example (shorthand)
#multiples_of_three = [x for x in range(1,31) if x % 3 == 0]
numbers = list(range(1,31))

threes = [x for x in numbers if x % 3 == 0]

print(threes)