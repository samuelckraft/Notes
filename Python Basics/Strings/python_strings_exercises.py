#Task 1

#First attempt
#def find_character_index(text, character):
#    text = input("Input a string: ")
#    character = input("Which character do you want the index of? ")
#    if character.lower() not in text.lower():
#        print("Character is not present")
#    else:
#        print(f"The index of {character} is {text.index(character)}")

def find_character_index(text, character):
    if len(character) == 1:
        index = text.find(character)
        if index == -1:
            return f"The character {character} is not present in the text."
        else:
            return f"The index of the character '{character}' is: {index}"
    else:
        return "Please enter only a single character."
    
while True:
    text_input = input("Enter a line of text from the book: ")
    char_input = input("Enter the character to find: ")

    result = find_character_index(text_input, char_input)
    print(result)

    continue_search = input("Do you want to search for another character? (yes/no) ").lower()
    if continue_search != 'yes':
        break


#Task 2
def generate_echo_text(text):
    if text:
        return ''.join([char * 2 for char in text]) #inside parentheses puts every letter into a list and doubles them, then the .join brings the list to one line
    else:
        return "The input text cannot be empty"
    
while True:
    text_input = input("Please input your draft: ")

    echo_text = generate_echo_text(text_input)
    print(f"Your echoed text is: {echo_text}")

    continue_echo = input("Do you want to create another echo text? (yes/no) ").lower()
    if continue_echo != 'yes':
        break


#Task 3
def format_highlights(highlight_string):
    if highlight_string.strip():
        return [play.strip() for play in highlight_string.split(',')]
    else:
        return []
    
while True:
    user_input = input("Enter the game highlights, separated by commas: ")
    formatted_highlights = format_highlights(user_input)

    if formatted_highlights:
        print("Game highlights: ")
        for play in formatted_highlights:
            print(f"- {play}")
    else:
        print("No highlights entered. Please provide the highlights of the game.")

    continue_input = input("Do you want to enter more highlights? (yes/no) ").lower()
    if continue_input != 'yes':
        break

#Task 4


#First attempt
#def announce_message(upper_string):
#    if upper_string:
#        return upper_string.upper()
#    else:
#        print("User input needed, please try again")
    
#while True:
#    user_input = input("Please enter string you want capitalized: ")
#    uppercased = announce_message(user_input)
#    print(f"Announcement: {uppercased}")

#    continue_input = input("Do you want to run another announcement? (yes/no) ").lower()
#    if continue_input != 'yes':
#        break

def announce_message(upper_string):
    return upper_string.upper()
    
while True:
    user_input = input("Please enter string you want capitalized: ")
    if user_input.strip():
        uppercased = announce_message(user_input)
        print(f"Announcement: {uppercased}")
    else:
        print("User input needed, please try again")

    continue_input = input("Do you want to run another announcement? (yes/no) ").lower()
    if continue_input != 'yes':
        break


#Task 5

#First attempt
#def create_welcome_message(users_name):
#    return f"Welcome **{users_name}**"

#while True:
#    user_input = input("Please enter your name: ")
#    if user_input.strip():
#        welcome_message = create_welcome_message(user_input)
#        print(welcome_message)
#    else:
#        print("No name entered, please try again")

#    continue_message = input("Is there another user to greet? (yes/no) ").lower()
#    if continue_message != "yes":
#        break

def create_welcome_message(users_name):
    line_length = 30
    centered_name = users_name.center(line_length, '*')
    return f"Welcome {centered_name} Welcome"

while True:
    user_input = input("Please enter your name: ")
    if user_input.isalpha():
        welcome_message = create_welcome_message(user_input)
        print(welcome_message)
    else:
        print("No name entered, please try again")

    continue_message = input("Is there another user to greet? (yes/no) ").lower()
    if continue_message != "yes":
        break


#Task 6
def print_stats(stats_string):
    stats_list = stats_string.split(';')
    for stat in stats_list:
        category_value = stat.split(':')
        if len(category_value) == 2:
            category, value = category_value
            print(f"Category: {category}, Value: {value}")
        else:
            print(f"Invalid format for stat: {stat}")
            break


while True:
    stats_input = input("Enter your stats, separated by semicolons (e.g. Goals:4;Assists:2;Fouls:1): ")
    print_stats(stats_input)
    
    continue_message = input("Would you like to enter more stats? (yes/no) ").lower()
    if continue_message != "yes":
        break


#Task 7
def swap_characters(username):
    if len(username) > 1:
        return username[-1] + username[1:-1] + username[0]
    return username

while True:
    username_input = input("Enter your username: ")
    username_switched = swap_characters(username_input)
    print(f"Your swapped username is: {username_switched}")

    continue_message = input("Is there another username you'd like to swap? (yes/no) ").lower()
    if continue_message != 'yes':
        break


#Task 8
def reverse_agenda(agenda_string):
    #'gym, breakfast, work'
    agenda_items = agenda_string.split(',') #takes whatever is put in the argument and splits wherever the comma is
    #['gym', 'breakfast', 'work']
    reversed_agenda = agenda_items[::-1]
    #['work', 'breakfast', 'gym']
    return ', '.join(reversed_agenda)
    #'work, breakfast, gym'

while True:
    user_agenda = input("Enter your tasks for the day divided by a comma: ")
    reversed_order = reverse_agenda(user_agenda)
    print(f"Your reversed tasks are: {reversed_order}")


    continue_input =input("Would you like to convert another agenda? (yes/no) ").lower()
    if continue_input != 'yes':
        break


#Task 9
def stylize_post(post):
    stylized_chars = []
    for symbol in post:
        if symbol == 'a':
            stylized_chars.append('@')
        elif symbol == 'e':
            stylized_chars.append('3')
        else:
            stylized_chars.append(symbol)
    return ''.join(stylized_chars)

while True:
    post_input = input("Please enter your post: ")
    stylized_post = stylize_post(post_input)
    print(f"Stylized post: {stylized_post}")

    continue_input = input("Would you like to stylize another post? (yes/no) ").lower()
    if continue_input != 'yes':
        break


#Task 10
def repeat_message(message, times):
    return '-'.join([message] * times)


while True:
    user_message = input("Enter the message you want to repeat: ")
    repeat_count = int(input("How many times would you like to repeat it? "))

    repeated_message = repeat_message(user_message, repeat_count)

    print(f"Repeated message: {repeated_message}")

    continue_input = input("Would you like to enter another message to repeat? (yes/no) ").lower()

    if continue_input != 'yes':
        break