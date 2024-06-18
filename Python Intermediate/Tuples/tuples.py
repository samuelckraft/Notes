#creating tuples

my_tuple = ("Fantasy", "Mystery", "Poetry")

tuple_2     =   "Epic", "Fable", "Legend"

tuple_3 = "Prologue", "Conflict", ["Climax", "Resolution"]

nested_tuple = ("Foreword", ("Chapter 1", "Chapter 2"), "Epilogue")

another_nested_tuple = ("Prologue", ("Conflict", ("Climax", "Resolution")), "Afterword")


#Accessing Tuples
    #indexes same as lists

print(my_tuple[0]) #output: Fantasy

print(another_nested_tuple[1][1][0]) #output: Climax

print(tuple_2[0:2]) #output: ('Epic', 'Fable')

    #dictionaries within tuples
enchated_library = ("Chapter 1", {"Mythical Creatures": ["Dragon, Unicorn"], "Legendary Places": ["Atlantis", "El Dorado"]}, "Chapter 2")

print(enchated_library[1]["Legendary Places"][1]) #Output: "El Dorado"
            #1 grabs the dictionary, legendary places grabs key for list, 1 pulls first index from that list


#Editing Tuples

new_tuple = ("Introduction", "Conclusion")

temp_list = list(new_tuple) #turns tuple into list ['Introduction', 'Conclusion']

temp_list.append("Epilogue")

new_tuple = tuple(temp_list) #turns list back to tuple under same name

print(new_tuple) #output: ('Introduction', 'Conclusion', 'Epilogue')

#unpacking

genres = ("Magic", "Mystery", "Myth")

genre1, genre2, genre3 = genres #always need a variable for every element in the tuple (can't have two variables but 3 values)

print(genre1) #output: Magic
print(genre2) #output: Mystery
print(genre3) #output: Myth

    #unpacking using astericks

book_parts = ("Prologue", "Adventure", "Climax", "Epilogue")

beginning, *middle, end = book_parts # '*' catches everything thats not in the beginning or end variable

print(beginning) #output: Prologue
print(middle) #output: [Adventure, Climax]
print(end) #output: Epilogue



#enumerate
    #returns tuple pair for every item
        #tuple pair is the item index and its value
chapters = ("The Lighthouse", "The Ministry of Truth", "The Trial")
        #(0,"The Lighthouse")(1,"The Ministry of Truth")(2,"The Trial")
for index, chapter in enumerate(chapters):
    print(f"Chapter {index+1}: {chapter}")


#looping with nested tuples
nested_tales = (("The Dawn", "The Noon"), ("The Dusk", "The Night"))

for pair in nested_tales:
    for tale in pair:
        print(tale)
        #Output:
        #The Dawn
        #The Noon
        #The Dusk
        #The Night


#looping through tuples nested with lists

mixed_collection = ("Poetry", ["Sonnet", "Haiku"], "Prose")

for element in mixed_collection:
    if isinstance(element, list):   #isinstance returns if a object (in this case element) is a part of a class or variable (like list, integer, etc.)
        for item in element:
            print(f"List Item: {item}")
    else:
        print(f"Tuple Element: {element}")

    #Output:
    # Tuple Element: Poetry
    # List Item: Sonnet
    # List Item: Haiku
    # Tuple Element: Prose



#looping through tuples with nested dictionaries

historical_records = ("Ancient", {"Rome": "Republic", "Greece": "Democracy"}, "Medieval")

for element in historical_records:
    if isinstance(element, dict):
        for key, value in element.items():
            print(f"{key}: {value}")
    else:
        print(element)

    #output:
    # Ancient
    # Rome: Republic
    # Greece: Democracy
    # Medieval

#count() and index()
literary_elements = ("Irony", "Metaphor", "Irony", "Symbolism")

print(literary_elements.count("Irony")) #output: 2

print(literary_elements.index("Metaphor")) #output: 1

#joining/repeating tuples
epic = ("Odyssey", "Iliad")
drama = ("Hamlet", "Othello")

literary_union = epic + drama

print(literary_union) #output: ('Odyssey', 'Iliad', 'Hamlet', 'Othello')

print(epic*3) #output: ('Odyssey', 'Iliad', 'Odyssey', 'Iliad', 'Odyssey', 'Iliad')