#Print function
    #new line in text \n
print("Are you ok?\nYes")

    #tab in text \t
print("Are you ok?\tYes")

    #put in backslash needs two \\ (first one says there is a special character, second one is the character itself)
print("this is a backslash \\")

    #example of how backslashes are used to keep the apostrophes there (mainly if the brackets of text match (either '' or ""))
print('She said \'Hello\'')

    #using the + for strings
greeting = "Hi"
name = "Sam"

print(greeting + ' ' + name)

    #can't print int in str so have to convert to text
age = 23
print(name + ' is ' + str(age) + ' years old')

    #end and sep function
print("apple", "banana", "orange", sep=" - ") #sep separates the items in the print function by whatever you set it equal to

print("This is the beginning... ", end='') #end combines two separate print functions (not sure why you wouldn't just use + but guess we'll see)
print("and this is the continuation") 

print("apple", "banana", "orange", sep=" - ", end="...yum")#combining both

print(' ')
    #Placeholders and f-strings
name = 'Sam'

print("My name is %s" % name) #% is placeholder and then it is defined at end

print("I am {}".format(name))

print(f"{name} is my name") #known as f string allows us to insert variables directly into the print

pi = 3.14159265
print(f"The value of pi to three decimal places is {pi:.3f}") #takes first three decimal places and rounds it up

print(' ')
print("end of print function section")
print(" ")

#Input function
    #always returns as a string, so if we need another data type we'd have to convert it
age = int(input("How old are you? "))

print(f'Next year you will be {age+1}')

    #can be used to determine flow of data
answer = int(input("What is 2+2? "))

if answer == 4:
    print("Good job")
else:
    print("How stupid are you?")

#Type() - len() - isinstance()
variable1 = "Sherlock"
variable2 = ["candlestick", "footprint", "handkerchief"]
variable3 = "I am a duke"

print("Type of variable1:", type(variable1)) #returns the data type of the variable
print("Number of items in variable2:", len(variable2)) #returns number of items in the list
print("Is the title genuine?", isinstance(variable3, str)) #returns true or false if item (Variable3) matches class/tuple (str)

print(" ")
#Number functions
import math

scores = [1,5,10,8,4,2]
    #abs() - absolute value
    #round() - rounds number to nearest whole value or to specified decimal space
    #sum() - pretty self explanatory
print(abs(-20), round(3.14159, 2), sum(scores))


    #min() and max() - returns smallest or largest numbers
    #pow() - to the power of
    #divmod() - divides and gives remainder
print(min(scores), max(scores), pow(2, 3), divmod(10,3)) #pow returns 8, meaning 2 to the 3rd power, and divmod returns (3,1), meaning 3 with a remainder of 1


    #sqrt() - returns square root
    #ceil() and floor() - ceil instantly rounds up to next higher number and floor instantly rounds down
print(math.sqrt(16), math.ceil(2.1), math.floor(2.9)) #ceil returns 3 and floor returns 2


    #exp() and log() - 
print(math.exp(1), math.log(10))


    #sin()/cos()/tan() - fuck these
angle = 360
print(math.sin(angle), math.cos(angle), math.tan(angle))


    #radians() and degrees() - convert between degrees and radians
print(math.radians(180), math.degrees(math.pi)) #these are basically just doing the opposite of each other