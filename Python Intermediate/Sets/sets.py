#creating sets

unique_party = {'Alice', 'Bob', 'Charlie'} #can be added to or removed from, but cannot edit individual elements

guest_list = set(['Alice', 'Bob', 'Charlie'])

list_guests = ['Alice', 'Bob', 'Alice', 'Charlie']

set_party = set(list_guests) #turns into set and automatically removes duplicate 'Alice'

tuple_guests = ('Alice', 'Bob', 'Charlie')

set_guests = set(tuple_guests)

dict_guests = {'name 1': 'Alice', 'name 2': 'Bob', 'name 3': 'Charlie'}

set_dict1 = set(dict_guests.values()) #output: {'Alice', 'Charlie', 'Bob'}
set_dict2 = set(dict_guests.keys()) #output: {'name 1', 'name 3', 'name 2'}


#looping through sets
for guest in unique_party:
    print(f"Welcome {guest}") #will print it in a different order each time since sets don't have ordered

if 'Alice' in unique_party:
    print("Alice is enjoying the party")
else:
    print("Alice isn't there")

for index, guests in enumerate(unique_party): #provides temporary structure/indexes to set
    print('Guest #', index, ' is ', guests)

for index, guest in enumerate(sorted(unique_party)): #puts output in alphabetical order
    print('Guest #', index, ' is ', guest)

#adding/removing
unique_party.add("Sam")

more_guests = ['Ethan', 'Fiona']

unique_party.update(more_guests) #adds multiple people at a time

unique_party.remove('Charlie') #removes specific value

unique_party.discard('Jonathan') #removes value if you're not sure it's in there

unique_party.pop() #randomly gets rid of a value

unique_party.clear() #clears entire list

#merging sets
set1 = {'Alice', 'Bob', 'Charlie'}
set2 = {'David', 'Emma', 'Charlie'}

grand_union = set1.union(set2) #output: {'Alice', 'Charlie', 'Emma', 'Bob', 'David'}

    #intersection is for finding the same value in 2 lists
mutual_friends = set1.intersection(set2) #output: {'Charlie'}

    #difference identifies different items from set 1 to set 2, not other way around
exclusive_friends = set1.difference(set2) #output: {'Alice'}

    #symmetric difference finds people who are in one of the two sets
unique_attendees = set1.symmetric_difference(set2) #output: {'David', 'Emma', 'Alice', 'Bob'}


#set comprehension

square_party = {a**2 for a in range(6)} #output: {0, 1, 4, 9, 16, 25}

print(square_party)