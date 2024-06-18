#classes defines the structure and behavior of an object
#object is a specific instance of a class

    #class variables
    #instance variables

#constructor

#deconstructor
class OfficeBuilding:
    def __init__(self, floors, offices):
        self.floors = floors
        self.offices = offices

    def open_doors(self):
        print('Doors are open for business')


building1 = OfficeBuilding(10,200)
building2 = OfficeBuilding(20, 400)

building1.open_doors()

#Example?

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def lend_book(self, title):
        book = self.find_book(title)
        if book and book.check_out():
            print(f"Book '{title}' has beeen lent out")
        else:
            print(f"Book '{title}' is not available")
    
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"Book '{title}' has been returned")
        else:
            print(f"Book '{title}' not found in library")

library = Library()

while True:
    action = input('Enter action (add, lend, return, search, exit): ').lower()

    if action == 'exit':
        break

    try:
        if action == 'add':
            title = input('Enter the book title: ')
            author = input('Enter book author: ')
            library.add_book(Book(title, author))
            print(f"Added book '{title}'")
        elif action == 'lend':
            title = input('Enter book title to lend: ')
            library.lend_book(title)
        elif action == 'return':
            title = input('Enter book title to return: ')
            library.return_book(title)
        elif action == 'search':
            title = input('Enter book title to search: ')
            book = library.find_book(title)
            if book:
                availability = 'available' if book.is_available else 'not available'
                print(f"'{title}' by {book.author} is {availability}")
            else:
                print(f"Book '{title}' not found")
    except Exception as e:
        print(f"An error occured: {e}")

print('Library system closed')