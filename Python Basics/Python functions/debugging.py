#syntax errors - grammatical mistakes = a clear error message
#runtime errors - followinga  map = finding a road that isn't there
#logical errors - outcome not expected

#pdb - a gps for your code helping you navigate, pause and inspect
#import pdb ----> pdb.set_trace()

import pdb

def add_numbers(n):
    total = 0
    for i in range(n):
        pdb.set_trace() #n - goes to next line: c - goes to next command: q - quit
        total +=1
    return total

print(add_numbers(5))