    #basics

    #text files are stored data that humans can read as opposed to binary files which are much more complex

# file = open('my_garden.txt', 'w') #must give file name and file mode
# print(file)
    #file name/paths
        #Above is an example of a relative path
            #if it was in a different folder, would need to put open('Folder1\\Folder2\\my_garden.txt', 'w')
            #also use ./ for current directory, or ../ if you need to go back a directory (like going from assignments to coding) and ../../ if you need to go back 2 dir. etc.
        
        #absolute path is the same function but instead of folder1\\folder2 it's 
            #c:/Users/Samuel/OneDrive/Documents/OneDrive/Documents/Coding/F-around/F-around/Python Intermediate/File Handling/file_handling.py
            #can be seen by hovering over file in the workspace

    #file modes (if file doesnt exist, w and a will create a new file but r will raise an error)
        #'r' for reading files
        #'w' for writing files
        #'a' for appending (adding onto files)
        #'r+', 'w+', 'a+' for both reading and writing

    #closing files is essential
# file.close()
# print(file.closed) #prints True if file is closed


#with statement

#with open('my_garden.txt', 'r') as file:
    #read the file
    #The file is automatically closed here, outside the block

#with open('my_garden.txt', 'r') as file1, open('garden_notes.txt', 'w'):
    #read the file1
    #write to the file2
    #both files are automatically closed here


    #Reading/writing files

    #Absolute reference
# with open('c:/Users/Samuel/OneDrive/Documents/OneDrive/Documents/Coding/F-around/F-around/Python Intermediate/File Handling/test.txt', 'w') as file:
#     file.write("Today I planted corn")

# with open('test.txt', 'w') as file:
#     file.write("Today I planted corn")

# with open('test.txt', 'a') as file:
#     file.write('\nNote: Water the plants')


# from datetime import date

# with open('test.txt', 'a') as file:
#     file.write(f'\n{date.today()}: Pruned the bushes')


# with open('test.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# with open('test.txt', 'r') as file:
#     content = file.read()
#     print(content)



    #File handling using loops and conditional statements

# with open('test.txt', 'r') as file:
#     for line in file:
#         if 'Pruned' in line:
#             print(line.strip())

    #lists
# flowers = ['Sunflowers', 'Rose', 'Lavendar']

# with open('test.txt', 'a') as file:
#     for flower in flowers:
#         file.write('\n' + flower + '\n')

# flowers = []
# with open('test.txt', 'r') as file:
#     for line in file:
#         flowers.append(line.strip())
# print(flowers)

    #dictionaries
# garden_care = {
#     'Sunflower': 'full sun',
#     'Rose': 'prune regularly',
#     'Lavendar': 'well-drained soil'
#     }
# with open('test.txt', 'w') as file:
#     for plant, care in garden_care.items():
#         file.write(f'{plant}: {care}\n')

# garden_care = {}
# with open('test.txt', 'r') as file:
#     for line in file:
#         plant, care = line.strip().split(': ')
#         garden_care[plant] = care
# print(garden_care)


    #tuple
# tools = ('Spade', 'Rake', 'Hoe')
# with open('test.txt', 'w') as file:
#     file.write(', '.join(tools))


# with open('test.txt', 'r') as file:
#     tools = tuple(file.read().strip().split(', '))
# print(tools)


    #sets
# unique_flowers = {'Sunflower', 'Rose', 'Daisy'}
# with open('test.txt', 'w') as file:
#     for flower in unique_flowers:
#         file.write(flower + '\n')

# unique_flowers = set()
# with open('test.txt', 'r') as file:
#     for flower in file:
#         unique_flowers.add(flower.strip())
# print(unique_flowers)


    #seek() and tell()

    #tell
# with open('test.txt', 'r') as file:
#     first_position = file.read(32) #read the first 32 characters
#     position = file.tell() #tells us our current position in the file
#     print(f'We are at position: {position}')
#     second_part = file.read(45)
#     position = file.tell()
#     print(f'We are at position: {position}')
#     print(f'First part: {first_position}')
#     print(f'Second part: {second_part}') #picks up where the first part leaves off

    #seek()
# with open('test.txt', 'r+') as file:
#     file.seek(0) #move to the beginning of the file
#     first_line = file.readline()
#     print(f"The first line of the file is: {first_line}")

# with open('test.txt', 'r+') as file:
#     file.seek(14) #move to the position we want to change
#     file.write("\nUpdated list")


    #OS

#creating directory

import os

# os.makedirs('my_test_files', exist_ok=True) 

# print("created a new directory for test files")



#Path manipulation

# old_path = 'test.txt'

# new_path = os.path.join('my_test_files', 'test.txt')

# os.rename(old_path, new_path)
# print(f"Moved {old_path} to {new_path}") #output: Moved test.txt to my_test_files\test.txt


#checking if path exists
new_path = os.path.join('my_test_files', 'test.txt')

if os.path.exists(new_path): #output: success
    print("Success")
else:
    print("Failure")
    
    #Other OS methods

    #os.listdir() - list contents of directory

    #os.remove() - removes files

    #os.path.isfile() and os.path.isdir() - checks if file/directory exists

print(os.listdir('my_test_files'))