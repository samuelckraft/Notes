#Task 1
time = int(input("How many seconds is the countdown? "))

while time >= 0:
    print("There is " + str(time) + " seconds left")
    time -= 1
print(" ")

#could also do it this way
timer = 10

while timer > 0:
    print(timer)
    timer -= 1

print(" ")

#Task 2
your_number = int(input("What is your order number? "))
current_order = 0

while your_number > current_order:
    current_order += 1
    print("Calling order " + str(current_order) + "!")

print(' ')

#Task 3
charge_level = 0

while charge_level <= 100:
    charge_level += 10
    print("Battery is now at " + str(charge_level))

    if charge_level == 50:
        print("Battery is charged to half capacity")
    elif charge_level == 80:
        print("Charge will last half a day")

print("battery is now fully charged")

print(" ")

#Task 4
cups_left = 10
coffee = ["French Vanilla", "Espresso", "Cappucino", "Latte", "Frap"]

while cups_left > 0:
    if coffee:
        dispensing = coffee.pop(0)
        print(f"Dispensing: {dispensing}")
        cups_left -= 1
        print(f"Coffee types left: {coffee}")
    else:
        print("Add coffee")
        break
#First attempt
#while cups_left > 0:
#    cups_left -= 1
#    for x in coffee:
#        print("Now dispensing " + x)
print(" ")
    
#Task 5
#current_floor = 3
#requested_stops = [1,3,5]

#while current_floor > 0:
#    for a in requested_stops:
#        if a < current_floor:
#            print(f"Stopping at floor {current_floor}")
#            requested_stops.remove(current_floor)
#            current_floor -= 1
#        else:
#            print(f"Stopping at floor {current_floor}")
#            requested_stops.remove(current_floor)
#            current_floor += 1

#Task 6
lights = ['red', 'yellow', 'green', 'yellow']
greens = 0

while True:
    for x in lights:
        print(f"The traffic light is now {x}")
        if x == 'green':
            greens += 1
            if greens == 3:
                print("Maintenance required")
                break
    if greens == 3:
        break

print(" ")

#Task 7
count = 10

landed_numbers = []

while count > 0:
    count -= 1
    if count %2 != 1:
        continue
    landed_numbers.append(count)

print("Numbers landed on: ", landed_numbers[::-1])