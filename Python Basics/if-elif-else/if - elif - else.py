#Exercise 1
Light = input("Enter traffic light color:")

if Light == "Red":
    print("Stop")
elif Light == "Yellow":
    print("Slow down")
elif Light == "Green":
    print("Gun it")


#Exercise 2
age = int(input("Enter age: "))
rating = input("Movie rating: ")
#G=1, PG=2, PG-13=3 and R=4
if age >= 5 and rating == "G":
    print("Allowed")
elif age>=7 and rating == "PG":
    print("Allowed")
elif age>=13 and rating == "PG-13":
    print("Allowed")
elif age>=17 and rating == "R":
     print("Allowed")

else: print("You're too young")

#Exercise 3
temp = int(input("Temp = "))

if temp<=50:
    print("Dress warm")
elif 51<=temp<=100:
    print("shorts and a t-shirt")
elif temp>=100:
    print("OMG it burns")

#Exercise 4
grade = int(input("Grade: "))

if grade <= 60:
    print("F")
elif 60<=grade<=69:
    print("D")
elif 70<=grade<=79:
    print("C")
elif 80<=grade<=89:
    print("B")
elif 90<=grade<=100:
    print("A")

#Exercise 5
activity = int(input("Minutes spent exercising: "))

if activity <= 15:
    print("You're gonna die young")
elif 15<=activity<=30:
    print("Not bad, but not great")
elif 30<=activity<=45:
    print("Doing good")
elif 45<=activity:
    print("Absolutely great")

#Exercise 6
likes_sugar = input("Do you like sugar (yes/no): ")
likes_milk = input("Do you like milk (yes/no): ")

if likes_sugar == "yes" and likes_milk == "yes":
    print("What are you a child")
elif likes_sugar == "yes" and likes_milk == "no":
    print("Gonna die of diabetes")
elif likes_sugar == "no" and likes_milk == "yes":
    print("Better use skim")
elif likes_sugar == "no" and likes_milk == "no":
    print("Finally a real man")

#Exercise 7
days_overdue = int(input("Days overdue: "))
fine = 0

if days_overdue <= 5:
    fine = days_overdue*1
elif days_overdue<=10:
    fine = days_overdue*2
else:
    fine = days_overdue*5

print(f"Your fine is ${fine}.")