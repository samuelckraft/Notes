#keys (home address) and values (whats in the house)
#Spoons/plates/cups are keys, top drawer/middle shelf/top shelf are values
kitchen = {
    "Spoons" : "Top Drawer",
    "Plates" : "Middle Shelf",
    "Cups" : "Top Shelf"
}
print(kitchen)

location_of_spoons = kitchen["Spoons"] #key points to value
print(location_of_spoons) #output: top drawer

#get function
location_of_toaster = kitchen.get("Toaster", "Not found") #instead of giving key error since value not in dictionary, allows you to put in a default value
print(location_of_toaster) #output: Not found

#Adding/updating elements
community_center = {
    "Yoga":"8 AM",
    "Art":"10 AM"
}

community_center["Cooking"] = "1 PM" #Key on left, value on right
community_center["Yoga"] = "6 AM"
print(community_center) #Ouput: {'Yoga': '6 AM', 'Art': '10 AM', 'Cooking': '1 PM'}

#Removing elements

    #pop() method
    #pop(key, [default])
inventory = {"Apples" : 30, "Oranges" : 20, "Bananas" : 15}
removed_item = inventory.pop("Oranges")
non_existent_item = inventory.pop("Strawberry", "item not found")
print(removed_item) #output: 20
print(non_existent_item) #output: item not found
print(inventory)#output: {'Apples': 30, 'Bananas': 15}

    #popitem() method
    #automatically grabs and removes last item added
user_data = {"name":"Alice", "age":30, "city":"New York"}

removed_item = user_data.popitem()
print(removed_item) #output: ('city', 'New York')
print(user_data) #output: {'name': 'Alice', 'age': 30}

    #del method
    #del dictionary[key]

book_shelf = {"Fiction":10, "Non-Fiction":7, "Mystery":5}

del book_shelf["Non-Fiction"] #if value not in dictionary will throw Key Error
print(book_shelf) #output: {'Fiction': 10, 'Mystery': 5}

    #clear() method
    #clears out whole dictionary
session_data = {"user ID":12345, "status" : "active", "Theme" : "dark"}
session_data.clear()
print(session_data) #output: {}


#Iterating over dictionary

    #items() method

book_ratings = {"1984" : 4.5, "To Kill A Mockingbird" : 4.8, "Brave New World" : 4.3}
    #key    value
for book, rating in book_ratings.items(): #if .items() not there it returns a ValueError
    print(f"{book} has a rating of {rating}")

    #Output:
    #1984 has a rating of 4.5
    #To Kill A Mockingbird has a rating of 4.8
    #Brave New World has a rating of 4.3


    #keys()/values() method

user_profile = {"Name" : "Alice", "Age" : 30, "Email" : "alice@example.com"}

for key in user_profile.keys(): #only prints off keys, not values
    print(key) 
    #output:
    #Name
    #Age
    #Email

for value in user_profile.values(): #only prints off values, not keys
    print(value)
    #Output:
    #Alice
    #30
    #alice@example.com




    #looping through in a particular order
colors_count = {"Red": 3, "Blue": 4, "Green": 1}

for color in sorted(colors_count.keys()): #sorts by alphabetical order
    print(f"{color}: {colors_count[color]}")
    #Output: 
    #Blue: 4
    #Green: 1
    #Red: 3

for color in sorted(colors_count.values()): #sorts by numerical order
    print(f"{color}")

    #Output:
    #1
    #3
    #4


#Update method
    #merges another dictionary or iterable of key-value pairs into the current dictionary

default_settings = {"theme": "light", "notifications": "on"}
user_settings = {"theme": "dark"}
default_settings.update(user_settings) #enter key and new value (if key/value pair exists, it will update it, if not, it will add it)
print(default_settings) #Output: {'theme': 'dark', 'notifications': 'on'}


#Setdefault() method
    #if key exists, will return value, else will add key/value to dictionary
stock = {"apples": 30, "oranges": 20}
stock.setdefault("bananas", 0) #if only key and no value given, will input None for value
value = stock.setdefault("apples")
print(value) #output: 30
print(stock) #output: {'apples': 30, 'oranges': 20, 'bananas': 0}


#Copying Dictionaries


    #shallow copy
original_artists = {"Picasso": 1881, "Van Gogh": 1853, "Monet": 1840}
copied_artists = original_artists.copy() #creates own separate dictionary that you can change without changing original

copied_artists["Van Gogh"] = 1900

print(f"Original: {original_artists}") #output: Original: {'Picasso': 1881, 'Van Gogh': 1853, 'Monet': 1840}
print(f"Shallow Copy: {copied_artists}") #output: Shallow Copy: {'Picasso': 1881, 'Van Gogh': 1900, 'Monet': 1840}


    #deep copy
import copy
original_paintings = {"The Starry Night": "Van Gogh", "The Scream": "Munch"}
reproduced_paintings = copy.deepcopy(original_paintings)

reproduced_paintings["The Starry Night"] = "Da Vinci"

print("Original: ", original_paintings)
print("Reproduced: ", reproduced_paintings)


#Lists within dictionaries

library = {
    "Fantasy": ["Harry Potter", "The Hobbit"], 
    "Science Fiction": ["Dune", "Neuromancer"], 
    "Mystery": ["Sherlock Holmes", "And then there were none"]
}

    #to add items to lists
library["Fantasy"].append("The name of the wind")

    #iterate over lists in dictionary
for book in library["Science Fiction"]:
    print(book) 
    #output:
    #Dune
    #Neuromancer

    #iterate over entire dictionary
for genre, books in library.items(): #genre is key, books is item
    print(f"Genre: {genre}")
    for book in books: #iterates through item
        print(f"- {book}")
        #output:
        #Genre: Fantasy
        #- Harry Potter
        #- The Hobbit
        #- The name of the wind
        #Genre: Science Fiction
        #- Dune
        #- Neuromancer
        #Genre: Mystery
        #- Sherlock Holmes
        #- And then there were none

#Dictionaries inside lists

art_gallery = [
    {"Title": "Starry Night", "Artist": "Van Gogh", "Year": 1889},
    {"Title": "The Scream", "Artist": "Munch", "Year": 1893},
    {"Title": "Guernica", "Artist": "Picasso", "Year": 1937},
]

art_gallery.append({"Title": "The Persistence of Memory", "Artist": "Dali", "Year": 1931})


for artwork in art_gallery: #artwork is the individual dictionary, and can now reference artist/title/year
    print(f"Title: {artwork['Title']}, Artist: {artwork['Artist']}, Year: {artwork['Year']}") #only works because every dictionary has artist, title and year as keys
    #Output
    #Title: Starry Night, Artist: Van Gogh, Year: 1889
    #Title: The Scream, Artist: Munch, Year: 1893
    #Title: Guernica, Artist: Picasso, Year: 1937
    #Title: The Persistence of Memory, Artist: Dali, Year: 1931



#Nested Dictionaries

museum_exhibits = {
    "Ancient Egypt": {
        "Artifacts": ["Sphinx", "Pyramids"],
        "Famous Pharaohs": ["Tut", "Cleopatra"]
    },
    "Rennessaince Art": {
        "Notable Artists": ["Da Vinci", "Michaelangelo"],
        "Key Works": ["Mona Lisa", "The Last supper"]
    }
}

museum_exhibits["Ancient Egypt"]["Recent Discoveries"] = ["New Tomb", "Ancient Scrolls"]

print(museum_exhibits["Ancient Egypt"]) #output: {'Artifacts': ['Sphinx', 'Pyramids'], 'Famous Pharaohs': ['Tut', 'Cleopatra'], 'Recent Discoveries': ['New Tomb', 'Ancient Scrolls']}

for exhibit, details in museum_exhibits.items():
    print(f"Exhibit: {exhibit}")
    for section, items in details.items():
        print(f"{section}: {', '.join(items)}")
        #output:
        #Exhibit: Ancient Egypt
        #Artifacts: Sphinx, Pyramids
        #Famous Pharaohs: Tut, Cleopatra
        #Recent Discoveries: New Tomb, Ancient Scrolls
        #Exhibit: Rennessaince Art
        #Notable Artists: Da Vinci, Michaelangelo     
        #Key Works: Mona Lisa, The Last supper