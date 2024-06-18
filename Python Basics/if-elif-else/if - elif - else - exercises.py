#Exercise 1
mood = input("What mood are you in? ")
weather = input("What is the weather like? ")

if mood == "happy":
    if weather == "sunny":
        print("Comedy")
    elif weather != "sunny": print("Romantic")
elif mood == "sad":
    print("Drama")
else:
    print("Adventure")

#Exercise 2
temp = float(input("What is the temperature? "))
event = input("What type of event is it? (formal, casual, other) ")

if temp < 15:
    if event == "formal":
        print("Wear a warm formal suit")
    elif event == "casual":
        print("Wear a cozy sweater and jeans")
elif temp >= 15:
    if event == "formal":
        print("Wear a light formal suit")
    else:
        print("Wear a t-shirt and shorts")

#Exercise 3
grade = input("What is your current grade? (A/B/C) ")
activity = input("Are you apart of a team/club? (sports/drama/neither) ")

discount = 0

if grade == "A":
    if activity == "sports":
        discount = 20
    elif activity != "sports":
        discount = 10
elif grade == "B":
    if activity == "drama":
        discount = 15
else:
    discount = 0

print(f"You are eligible for a {discount}% discount")

#Exercise 4
age = float(input("How old are you? "))

print("You can drive!") if age >= 18 else print("Not yet!")

#Exercise 5
protein = input("Do you prefer vegetarian or meat? ")
sugar = input("Would you like a sugar-free or regular? ")

if protein == "vegetarian":
    if sugar == "sugar-free":
        print("Fruit cup it is!")
    else:
        print("Veg cake it is!")
else:
    if sugar == "sugar-free":
        print("Sugar free ice cream it is!")
    else:
        print("Chocolate brownie it is!")