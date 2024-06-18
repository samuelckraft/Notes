#Strings are immuteable, meaning they cannot be changed directly
original_score = "Python" #if you wanted to change it to spell "Pithon" without actively changing this variable, we would have to create a new string
    #trying to do this directly by doing original_score[1] = i would create a type error
new_score = original_score[0] + "i" + original_score[2:]

where_is_p = original_score.index("P")
print(where_is_p)
print(original_score)
print(new_score)

print(' ')

#Iterating and slicing
track = "marathon"
for x in track:
    print(x, end=' ')    #iterating over marathon likee a list using a for loop and adding a space after each character
print(' ')
first_slice = track[0:3] #slices UP TO third index (meaning takes first 3 characters) - output: mar
second_slice = track[4:] #slices from fourth index to the end - output: thon
third_slice = track[2::2] #slices starting from second index and grabbing every second character - output: rto
print(first_slice)
print(second_slice)
print(third_slice)

game_plan = "Execute play number 9" #iterating with slicing

for word in game_plan[8:]:
    print(word, end=' ')

print(' ')

#String concatenation (basically just bringing multiple strings together)
quarterback = "Tom"
receiver = "Jerry"
play = " runs a route to catch the pass from "

complete_play = receiver + play + quarterback 

print(complete_play)

players = ["Python", "is", "great", "for", "string", "manipulation"]

team_statement = ""

for word in players:
    team_statement += word + " "

print(team_statement.strip()) #.strip removes extra spaces

qb = "Player"
jersey_number = 10
message = " scored a "
points = 6
summary = " points!"

highlight_reel = qb + " " + str(jersey_number) + message + str(points) + summary

print(highlight_reel)

#String Formatting
celebration = "{} scores a touchdown and does the {} dance"

touchdown_celebration = celebration.format("Tom", "moonwalk")

print(touchdown_celebration)

player = "Tom"
action = "touchdown"
celebration_move = "moonwalk"

play_call = f"{player} scores a {action} and does the {celebration_move}"

print(play_call)

print(' ')

#upper() and lower()
chant = "Go team!"

loud_chant = chant.upper()
quiet_chant = chant.lower()

print(loud_chant)
print(quiet_chant)

#replace/strip/join/split
game_plan = "Attack from the left flank"

new_plan = game_plan.replace("left", "right")
print(new_plan)

player_name = "  Ronaldo  "
clean_name = player_name.strip() #removes leading and trailing whitespace

print(f"{clean_name} is ready to play")

cheer = "Here we go, team, here we go!"

words = cheer.split() #will default to split at any whitespace, but can be customized to split at specific characters

new_chant = "-".join(words)
print(words) #output: ['Here', 'we', 'go,', 'team,', 'here', 'we', 'go!']
print(new_chant) #output: Here-we-go,-team,-here-we-go!

team = cheer.find("team")
print(team) #returns 12 because that is the index right before team

total_words = cheer.count("we") #returns 2 because there is two instances of "we"
print(total_words)

print(cheer.startswith("Here")) #returns True or false if it starts with it or not
print(cheer.endswith("!")) #returns True or false if it ends with it or not

print(" ")

#isalpha(), isdigit(), isspace()
alpha = "words"
digit = "10"
space = " "

print(alpha.isalpha()) #returns true if variable is alphabetical
print(digit.isdigit()) #returns true if variable is numerical
print(space.isspace()) #returns true if variable is whitespace