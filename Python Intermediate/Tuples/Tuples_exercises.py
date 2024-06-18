#Task 1
def add_product(catalog):
    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        catalog.append((name, price, category))
    except ValueError:
        print("Invalid input, price must be a number")

def display_catalog(catalog):
    for product in catalog:
        print(f"Name: {product[0]} - Price: {product[1]} - Category: {product[2]}")

def search_category(catalog):
    category = input("Enter category to search: ")
    found = [product for product in catalog if product[2].lower() == category.lower()]
    if found:
        for product in found:
            print(f"Name: {product[0]} - Price: {product[1]}")
    else:
        print("No product found in this category")

def main():
    catalog = [] #creates tuple through the add product function then inserts each item as a tuple into the list
    while True:
        print("\n1. Add a product")
        print("2. View Catalog")
        print("3. Search by category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(catalog)
        elif choice == '2':
            display_catalog(catalog)
        elif choice == '3':
            search_category(catalog)
        elif choice == '4':
            print("Exiting system")
            break
        else:
            print("Invalid entry please try again")

    print(catalog)

main()


#Task 2
def display_catalog(catalog):
    for book in catalog:
        print(f"Title: {book[0]} - Author: {book[1]} - Genre: {book[2]}")

def search_by_title(catalog):
    title = input("Enter title to search: ")
    found = False
    for book in catalog:
        if book[0].lower() == title:
            print(f"Title: {book[0]} - Author: {book[1]} - Genre: {book[2]}")
            found = True
            break
    if not found:
        print("Book not found")

def list_by_genre(catalog):
    genre = input("Enter genre to list books: ").lower()
    found = False
    for book in catalog:
        if book[2].lower() == genre:
            print(f"Title: {book[0]} - Author: {book[1]}")
            found == True
    if not found:
        print("No books found in this genre")


def main():
    catalog = (
        ("To Kill a Mockingbird", "Harper Lee", "Classic"),
        ("1984", "George Orwell", "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
        ("Brave New World", "Aldous Huxley", "Dystopian")
    )
    
    while True:
        print("\n1. View all books")
        print("2. Search by title")
        print("3. List by genre")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            display_catalog(catalog)
        elif choice == '2':
            search_by_title(catalog)
        elif choice == '3':
            list_by_genre(catalog)
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice please try again")

main()

#Task 3
def add_tasks(tasks):
    name = input("Enter employee's name: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (dd/mm/yyyy): ")
    tasks.append((name, description, deadline))

def display_tasks(tasks):
    for task in tasks:
        name, description, deadline = task
        print(f"Name: {name} - Description: {description} - Due: {deadline}")

def complete_tasks(tasks):
    task_to_remove = input("Enter description of completed task: ")
    for i, task in enumerate(tasks):
        if task[1] == task_to_remove:
            del tasks[i]
            print("Task completed and removed")
            break
        else:
            print("Task not found")

def main():
    tasks = []
    while True:
        print("\n1. Add a task")
        print("2. View Tasks")
        print("3. Complete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            complete_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid please try again")

main()