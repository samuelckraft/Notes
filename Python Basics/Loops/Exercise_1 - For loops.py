#Task 1
booth_types = ["Food", "Games", "Music", "Crafts"]
times = ["10 am", "1 pm", "3 pm", "5 pm"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

for x in range(len(booth_types)):
    booth = booth_types[x]
    time = times[x]
    item = items_needed[x]
    print(f"{booth} Booth - Schedule {time} - Item Needed: {item}")

print(" ")

#Task 2
students = 30
rows = 5

students_per_row = students//rows

for row in range(1, students_per_row+1):
    for seat in range(1, students_per_row+1):
        seat_number = (row-1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: Student {seat_number}")

print(" ")

#Task 3
item_prices = [2, 5, 10, 11, 13]

total_cost = 0

for x in item_prices:
    total_cost += x

print(f"Total cost: ${total_cost:.2f}") #:.2f means answer goes to two decimal places

print(" ")

#Task 4
table_size = int(input("Enter the size of the multiplication table: "))

for y in range(1, table_size + 1):
    for z in range(1, table_size + 1):
        product = y * z
        print(f"{product} \t", end="")
    print()

print(" ")

#Task 5
inventory = [["Apples", 5], ["Bananas", 2], ["Oranges", 0], ["Milk", 1], ["Eggs", 12]]

reorder = 3

for a in inventory:
    name, quantity = a
    if quantity < reorder:
        print(f"{name} needs to be reordered")

print(" ")

#Task 6
found_items = ["rum", "treasure", "eyepatch", "treasure", "parrot"]

#First attempt
for c in found_items:
    if c == "treasure":
        print("We found it boys! No need to go further")
        break
    else:
        print("We'll get it on the next island")

print(" ")

#Task 7

#First attempt
#email_subject = ["work", "wife", "spam", "promotion", "bills"]
#email_content = []

#for c in email_subject:
#    for b in email_content:
#        if c != "work" or "wife" or "bills":
#            continue
#        else:
#            if b != "overdue electric bill" or "promotion":
#                continue
#            print("Congrats")
emails = ["123@gmail", None, "345@gmail", None, "678@gmail"]

valid_emails = []

for x in emails:
    if x is None:
        continue
    valid_emails.append(x)

print("Valid emails: ", valid_emails)