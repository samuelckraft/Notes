import re
#literal/metacharacters

    # dot (.) - matches any character besides newline (\n)

    # caret (^) - anchor for the starting of a string

    # dollar ($) - anchor for the end of a string

    # asterisk (*) - matches zero or more of occurences of the pattern left to it; multiplier creating copies of the character before it

    # plus (+) - matches one or more occurences of the pattern left to it

    # question mark (?) - makes preceding character optional

    # backslash (\) - escapes special characters or signals a special sequence

        # \d - the digit hunter
d_test = "Contact us at 123-456-7890"

phone_number = re.search(r"\d{3}-\d{3}-\d{4}", d_test)

print(phone_number) #output: <re.Match object; span=(14, 26), match='123-456-7890'>

if phone_number:
    print("Phone number found: ", phone_number.group()) #output: Phone number found:  123-456-7890

year_search = "Event was held on 15/06/2001"

year_extraction = re.search(r"\b\d{4}\b", year_search)

if year_extraction:
    print("Year: ", year_extraction.group()) #output: Year: 2001

        # \D - non-digit detector

        # \w - finds word characters (letters, digits and underscores)
post = 'Loving the #Python and #Regex learning journey! #coding'
hashtags = re.findall(r"#\w+", post) #finds any word/character after the hashtag; if the plus wasn't there it would just grab #P, #R, #c

print(hashtags) #output: ['#Python', '#Regex', '#coding']

        # \W - non-word character identifier

        # \s - seeks out whitespace (spaces, tabs, newlines)

        # \S - non-whitespace finder

        # \b - marker for positions between a word and a non-word character
b_test = "Write a program to build a bridge but beware of the beehive"

b_answer = re.findall(r"\bb\w*e\b", b_test) #\b finds words that start with b,then any character in between and end with e

print(b_answer) #output: ['bridge', 'beware', 'beehive']

        # \B - identifies positions where a word boundary doesn't occur

        # \A - matches only the start of the string

        # \Z - matches only the end of the string, before the final newline
    # square bracket ([]) - selects one character from a set ([abc] can match 'a', 'b' or 'c' while [a-z] matches any lowercase letters)

    # pipe (|) - or operator; matches pattern before or after it

    # parentheses (()) - groups patterns together and captures them

    # curly braces ({}) - used to define the exact number of times a character or a pattern must occur for a match to be found


#regular expressions


    #re.findall() - retrieves all non-overlapping matches of a pattern in a string, returning them as a list
findall_test = "Contact us at support@example.com or sales@example.com"

emails = re.findall(r"[A-za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", findall_test)

print(emails) #output: ['support@example.com', 'sales@example.com']

    #re.search() - scans through a string, looking for any location where the pattern matches
email = 'user@example.com'

search_test = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email) #output: <re.Match object; span=(0, 16), match='user@example.com'>
print(search_test)
if search_test: 
    print("Valid email")
else:
    print("Invalid email")

    #re.match() - determines if the regex pattern matches at the beginning of a string
match_test = 'Hello World'

match_answer = re.match(r"^Hello", match_test) 

print(match_answer) #output: <re.Match object; span=(0, 5), match='Hello'>

if match_answer:
    print("The string starts with hello")


match_test2 = '@user123'

match_answer2 = re.match(r"@\w+", match_test2)

print(match_answer2) #output: <re.Match object; span=(0, 8), match='@user123'>

url = "https://www.example.com"

url_match = re.match(r"^(https|http)", url)

print(url_match) #output: <re.Match object; span=(0, 5), match='https'>

    #re.split() - splits a string by occurences of a pattern
split_test = "Python,Regex;Splitting-Examples. Fun, right?"

split_answer = re.split(r"[,;.\s]+", split_test)

print(split_answer) #output: ['Python', 'Regex', 'Splitting-Examples', 'Fun', 'right?']


csv_data = "Name,Age,Occupation"

fields = re.split(r",", csv_data)

print(fields) #output: ['Name', 'Age', 'Occupation']


    #\W+ splits at any sequence of non-word characters

sentence = "Hello, World! Welcome to Python"

parts = re.split(r"(\W+)", sentence)

print(parts) #output: ['Hello', ', ', 'World', '! ', 'Welcome', ' ', 'to', ' ', 'Python']


    #re.sub() - replaces occurences of the pattern in a string with a replacement string


phone1 = "Phone = +1 (123)456-7890"

standard_phone = re.sub(r"\D","", phone1) #removes anything thats not a digit and replaces it with a blank character

print(standard_phone) #output: 11234567890


html1 = "<p>This is <em>HTML</em> content! </p>"

clean_html = re.sub(r"<.*?>", "", html1)

print(clean_html) #output: This is HTML content!


date = "Todays date is 15/04/2021"

formatted_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", date) #grabs day, month and year in groups and rearranges them

print(formatted_date) #output: Todays date is 2021-04-15