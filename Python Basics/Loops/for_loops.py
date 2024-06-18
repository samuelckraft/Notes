#loops allow you to repeat a task multiple times without manually writing out each step

#for loop allows you to iterate over items in a list, tuple, string, or any iterable object

flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted caramel"]

for flavor in flavors:
    print("Yum I just sampled " + flavor + "!")

    #for - marks the start of the "for" loop
    #flavor - variable that takes the value of each item in the iterable; can be anything
    #flavors - our iterable object (in this case its a list)
    #indented line - anything indented is the scope of the loop and will be executed each iteration

print(" ")
#range function helps generate a sequence of numbers, specify the start, stop and even the step size
for i in range(3):
    print("Trying out flavor number " + str(i+1) + ": " + flavors[i])


print(" ")
#nested loops create combinations for multi-layered data
ice_cream = ["chocolate", "vanilla", "strawberry", "pistachio"]
toppings = ["sprinkles", "chocolate syrup", "whipped cream", "cherry"]

for x in ice_cream:
    for y in toppings:
        print("Let's try a scoop of " + x + "with some " + y + " on top!")

print(" ")
#special moves - break (the emergency exit), continue (the skip button), pass(placeholder)
ice_cream_flavors = ["chocolate", "vanilla", "strawberry", "mint chocolate chip", "pistachio"]

for z in ice_cream_flavors:
    if z == 'mint chocolate chip':
        print("My favorite! No need to taste further")
        break
    print("Trying " + z + " flavor.")

print(" ")

for a in ice_cream_flavors:
    if a == 'strawberry':
        continue
    print("Enjoying a scoop of " + a + ".")

print(" ")

for b in ice_cream_flavors:
    if b == 'vanilla':
        pass
    print("Sampling " + b + " now")