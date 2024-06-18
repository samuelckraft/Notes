#Healing is at index 0, invisibility at index 1...
potions = ["Healing", "Invisibility", "Strength"]
print(potions)

print(" ")
#using negative index numbers counts from the end
fav_potion = potions[-3]
print(fav_potion)

print(" ")
#can mix multiple types of data into a list, including other lists
random_list = [fav_potion, 42, potions, 3.9, "Text"]
print(random_list)

print(" ")
#can add more on end with <list name>.append or remove with <list name>.remove
potions.append("Flight")
print(potions)

random_list.remove(3.9)
print(random_list)

print(" ")
#can count duplicates in list with <list name>.count
flowers = ["rose", "lily", "rose", "tulip"]

dupes = flowers.count("rose")
print(dupes)

print(" ")
#can insert in list at desired location with <list name>.insert(<desired index>, "<variable to insert>")
#can switch variables with <list name>[<index you want to replace] = <new value>
insert = [1, 2, 3, 4, 5]

insert.insert(2, 9)
insert[2] = 6
print(insert)

print(" ")
#removing items
#can either remove with <list name>.remove(<specific value in list>)
#or <list name>.pop(<index value>) (no value removes last value)
removal = [1, 2, 3, 4, 5, 6]
removal.remove(3)
removal.pop()

print(removal)

print(" ")
#find position with <list name>.index(<specific value in list>)
find = [1, 2, 3, 4, 5, 6, 7]
four_index = find.index(4)

print(four_index)

print(" ")
#completely clear the list with <list name>.clear()
clean = [1, 2, 3, 4, 5]
clean.clear()

print(clean)

print(" ")
#sort lists with <list name>.sort() - this will put it in alphabetical/numerical order
order = ["C", "M", "B", "Z", "A"]
order.sort()

print(order)

number_order = [4, 3, 5, 99, 1]
number_order.sort()

print(number_order)

print(" ")

#to count number of items use len(<list name>)
count = len(order)

print(count)

print(" ")
#reverse order with <list name>.reverse()
flipped = [5, 4, 3, 2, 1]
flipped.reverse()

print(flipped)

print(" ")
#in and not in operator prints true or false if value is in the list
all_in = [1, 2, 3, 4, 5]

print(1 in all_in)
print(7 in all_in)
print(7 not in all_in)

print(" ")
#merging lists by <variable> = <list 1> + <list 2>
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

added = list_1 + list_2

print(added)

print(" ")

#can also just extend a list to include another by using <list 1>.extend(<list 2>)
list_1.extend(list_2)

print(list_1)

print(" ")
#combining a list into one cohesive part with join method <variable> = "".join(<list name>)
story_elements = ["Once ", "upon ", "a ", "time..."]

story = "".join(story_elements)

print(story)

print(" ")
#slicing lists - colon acts as separator
slicer = [1, 2, 3, 4, 5, 6]

segment_1 = slicer[1:3]
beginning_to_third = slicer[:3]
third_to_end = slicer[3:]

print(segment_1, beginning_to_third, third_to_end)