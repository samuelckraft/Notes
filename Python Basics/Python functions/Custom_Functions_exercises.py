#Task 1
import datetime

def morning_routine():
    print("Good morning")
    weather = ['rainy', 'sunny', 'rainy', 'cloudy', 'sunny', 'snow', 'rainy']
    todays_weather = weather[datetime.datetime.today().weekday()]
    #print(datetime.datetime.today().weekday()) - returns day (0 is monday 6 is sunday)
    #print(todays_weather) - returns 'snow' for some reason idk why it jumps to day 5
    if todays_weather == 'rainy':
        print("Don't forget to bring an umbrella")

    calendar_events = ['Gym', 'Meeting', 'Dentist', 'Lunch', 'Grocery shopping']
    todays_events = calendar_events[datetime.datetime.today().weekday()]

    print(f"Todays event: {todays_events}")

    unread_emails = 5
    if unread_emails > 0:
        print(f"You have {unread_emails} unread emails")

morning_routine()

print(" ")

#Task 2
def make_coffee(coffee_type = "espresso"):
    coffee_type = ["black coffee", "americano", "frap", "cappuccino", "mocha"]
    for x in coffee_type:
        print(f"Dispensing: {x}")
        if x == "cappuccino":
            print("Your favorite!")
        else:
            pass

make_coffee("black coffee")

print(' ')

#Task 3
def play_songs(song_list):
    for x in song_list:
        print(f"{x} is now playing")

song_num = int(input("How many songs do you want on this playlist?" ))

user_playlist = []

for i in range(song_num):
    song_name = input(f"Enter song {i + 1} ")
    user_playlist.append(song_name)

play_songs(user_playlist)

print(' ')

#Task 4
def track_expenses(*expenses):
    total_expenses = sum(expenses)
    print(f"The total expenses are: {total_expenses}")

    highest_expense = max(expenses)
    highest_spender = expenses.index(highest_expense)+1
    print(f"Person {highest_spender} is the highest spender with an expense of: {highest_expense}")

group_expenses = []

while True:
    expense_input = input("Enter an expense amount or 'done' to finish: ")
    if expense_input.lower() == 'done':
        break
    else:
        expense = float(expense_input)
        group_expenses.append(expense)

track_expenses(*group_expenses)

print(' ')

#Task 5
products = ['T-shirt', 'Jeans', 'Sneakers', 'Hat', 'Sunglasses', 'Jacket', 'Watch']

def manage_inventory():
    while True:
        print("\n Inventory Management System")
        print('1. View Inventory')
        print('2. Add Product')
        print('3. Remove Product')
        print('4. Exit')
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\\nCurrent Inventory: ")
            for x in products[:5]:
                print(x)
            if len(products) > 5:
                print("... and more")
        elif choice == "2":
            new_prodcut = input("Enter the name of the new product: ")
            products.append(new_prodcut)
            print(f"{new_prodcut} has been added to the inventory")
        elif choice == "3":
            product_to_remove = input("Enter the name of the product to remove: ")
            if product_to_remove in products:
                products.remove(product_to_remove)
                print(f"{product_to_remove} has been removed")
            else:
                print(f"{product_to_remove} not found in inventory")
        elif choice == "4":
            print("Exiting inventory management system")
            break
        else:
            print("Invalid entry, please choose again")

manage_inventory()


print(' ')

#Task 6
def split_payment(spent, number_of_friends):
    total_expenses = sum(spent)
    individual_share = total_expenses/number_of_friends
    return total_expenses, individual_share

spent = []
number_of_friends = int(input("How many friends are there? "))

while True:
    item = input("Enter an expense or 'done' to finish: ")
    if item.lower() == 'done':
        break
    spent.append(float(item))

total, share = split_payment(spent, number_of_friends)

print(f"\nTotal expenses: ${total:.2f}")
print(f"Each person must pay: ${share:.2f}")

print(' ')

#Task 7
phonebook_names = []
phonebook_numbers = []

def add_contact(name, number):
    global phonebook_names
    global phonebook_numbers
    phonebook_names.append(name)
    phonebook_numbers.append(number)

def display_contacts():
    global phonebook_numbers
    global phonebook_names
    for x in range(len(phonebook_names)):
        print(f"Name: {phonebook_names[x]}, Number: {phonebook_numbers[x]}")

while True:
    action = input("Choose an action: \n[A] Add Contacts \n[B] Display Contacts \n[C] Exit \n")
    if action == "A":
        name = input("Enter the contacts name: ")
        number = input("Enter the contacts number: ")
        add_contact(name, number)
    elif action == "B":
        display_contacts()
    elif action == "C":
        break
    else:
        print("Invalid action please choose again")

print(' ')

#Task 8
employees = []

def add_employee(name, age, department):
    global employees
    employees.append([name, age, department])

def calculate_average_age():
    global employees
    total_age = sum(employee[1] for employee in employees)
    return total_age/len(employees) if employees else 0

def display_employees():
    global employees
    for employee in employees:
        print(f"Name: {employee[0]}, Age: {employee[1]}, Department: {employee[2]}")

while True:
    action = input("Choose an action: [A] Add an employee, [B] Calculate average age, [C] Display employees, [D] Quit ").upper()
    if action == 'A':
        name = input("Enter the employees name: ")
        age = int(input("Enter the employees age: "))
        department = input("Enter the employees department: ")
        add_employee(name, age, department)
    elif action == 'B':
        average_age = calculate_average_age()
        print(f"The average age of the employees is: {average_age:.2f}")
    elif action == 'C':
        display_employees()
    elif action == 'D':
        break
    else:
        print("Invalid action. Please choose again")