#Defining a function
def greet_user():
    print("Hello user")

greet_user() #calls the function
print(' ')
    #parameters
def make_sandwich(bread_type, filling): #info in parentheses is the parameters, and what you put in when you run it has to be in the same order as your parameters regardless of order in statement
    print(f"Making a {filling} sandwich with {bread_type} bread")

make_sandwich("honey wheat", "turkey")
print(' ')
    #default parameter values
def brew_coffee(size="medium"):
    print(f"Brewing a {size} coffee")

brew_coffee() #this prints "Brewing a medium coffee"
brew_coffee("large") #this prints "Brewing a large coffee"
print(' ')
    #passing lists to python functions
def prepare_snacks(snack_list):
    for x in snack_list:
        print(f"Preparing {x}...")

movie_snacks = ['popcorn', 'chocolate', 'fruit', 'nachos']

prepare_snacks(movie_snacks)
print(' ')
    #*args allows you to attach any number of extra arguments onto your current formal parameters
def make_ice_cream(*flavors): 
    for x in flavors:
        print(f"Scooping {x} ice cream!")
make_ice_cream ("vanilla", "chocolate", "strawberry")
print(' ')
    #**kwargs is keyword arguments
def make_lunch(**ingredients):
    for item, quantity in ingredients.items(): #**kwarg is what allows us to do both item and quantity
        print(f"Adding {quantity} of {item} to the sandwich")

make_lunch(tomatoes = "3 slices", lettuce = "2 leaves", mayo = "1 squeeze") #needs some type of name and value for **kwarg
print(' ')
    #return values
def add_numbers(a, b):
    return a+b #return is not the same as print, just because it doesn't show up in the terminal doesn't mean the calculation didn't happen
                #return values end the funtion same as a break
add_numbers(5, 9)

    #catching the return value
result = add_numbers(5,9)
print(result)

print(' ')

    #multiple returns - only one return statement can be ran
def check_even(number):
    if number %2 == 0:
        return True
    else:
        return False
    
even = check_even(5)
print(even)

print(' ')

    #Returning multiple values
def get_details():
    name = "Sam"
    age = 30
    return name, age
person_name, person_age = get_details() #these variables only return because they match the commas/data of the return statement
print(person_name, person_age)

print(' ')
#Scope

    #Local scope means (to my understanding) variables inside a function are only variables for that function, not outside of it
def greet():
    message = "Hello world"
    print(message)

greet() #returns hello world, but if I were to say print(message) nothing would return

print(' ')

    #Global scope means (to my understanding) that variables outside of the function can still be used in a function
name = "Sam"

def say_hello():
    print(f"Hello {name}")

say_hello() #if a local and global variable share a name, local variables will always take priority

print(' ')

    #Global keyword allows you to change global variables inside a function
counter = 0

def increment():
    global counter
    counter += 1

increment()

print(counter)

print(' ')

#Pass in functions

def calculate_interest():
    pass #TODO implement interest calculation

def upcoming_feature():
    pass #placeholder for a future feature

def unfinished_logic():
    pass #sub for incomplete logic

calculate_interest()
upcoming_feature()
unfinished_logic()

