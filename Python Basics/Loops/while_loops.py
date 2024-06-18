#while loops continue to execute as long as a certain condition holds true
marshmallows = 0

while marshmallows < 3:
    marshmallows += 1 #can adjust this line to before or after the print commmand, changing the output from adding the "marshmallow" before the print to adding it after
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows!")

print(" ")
#non-started loop where initial condition is never true
temp = 100

while temp < 0:
    temp += 1
    print("Temp = ", temp)
print("Temp was never below 0 to begin with")

#infinite loop happens when there is no stop signal, like a specific range or break statement
while True:
    user_input = input("Say 'stop' to end the refill: ") #will continue to ask for input until you say stop
    if user_input.lower() == 'stop':
        break
    else:
        print("Heres more coffee")