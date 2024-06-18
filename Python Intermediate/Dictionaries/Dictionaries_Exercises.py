#Task 1
def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"Category '{category}' added")
    else:
        print(f"Category '{category}' already exists")

def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"Product '{product}' added to '{category}'")
        else:
            print(f"Product '{product}' already exists in '{category}'")

    except KeyError:
        print(f"Category '{category}' does not exist")

def display_categories(catalog):
    for catagory, products in catalog.items():
        print(f"{catagory}: {', '.join(products)}")

def search_product(catalog, product):
    found = False
    for catagory, products in catalog.items():
        if product.lower() in [p.lower() for p in products]:
            print(f"Product '{product}' found in '{catagory}'")
            found = True
            break
    if not found:
        print(f"Product '{product}' not found")

catalog  = {
    "Electronics": ["Laptop", "Smartphone"],
    "Books": ["Fiction", "Non-Fiction"]
}

add_category(catalog, "Clothing")
add_product(catalog, "Electronics", "Camera")
display_categories(catalog)
search_product(catalog, "Laptop")
print(catalog)


#Task 2
def add_platform(content_dict, platform):
    if platform not in content_dict:
        content_dict[platform] = {}
        print(f"Platform '{platform}' added")
    else:
        print(f"Platform '{platform}' already exists")

def add_post_type(content_dict, platform, post_type):
    if platform in content_dict:
        if post_type not in content_dict[platform]:
            content_dict[platform][post_type] = []
            print(f"Post type '{post_type}' added to {platform}")
        else:
            print(f"Post type '{post_type}' already exists in {platform}")
    else:
        print(f"Platform {platform} does not exist")

def add_post(content_dict, platform, post_type, post):
    if platform in content_dict and post_type in content_dict[platform]:
        content_dict[platform][post_type].append(post)
        print(f"Post added to {platform} under {post_type}")
    else:
        print(f"Either platform {platform} or post type {post_type} does not exist")


def display_contents(content_dict):
    for platform, post_types in content_dict.items():
        print(f"Platform: {platform}")
        for post_type, posts in post_types.items():
            print(f"    Post type: {post_type}")
            for post in posts:
                print(f"        -{post}")

social_media_content = {
    "Facebook": {
        "Text": ["Hello world", "Python is fun"],
        "Image": ["Beach Photo", "Birthday party"]
    }
}


add_platform(social_media_content, "Instagram")
add_post_type(social_media_content, "Instagram", "Image")
add_post(social_media_content, "Instagram", "Image", "Sunset View")
display_contents(social_media_content)


#Task 3

def add_category(menu, category):
    if category not in menu:
        menu[category] = []
        print(f"Category '{category}' added")
    else:
        print(f"Category '{category}' already exists")

def add_item(menu, category, item):
    if category in menu:
        if item not in menu[category]:
            menu[category].append(item)
            print(f"Item {item} added to {category}")
        else:
            print(f"{item} already exists in {category}")
    else:
        print(f"{category} already exists")


def take_order(menu, order):
    try:
        order_items = [menu[category][item_index] for category, item_index in order]
        return order_items
    except (KeyError, IndexError):
        print("Invalid order, please check the menu and try again")

def display_menu(menu):
    for category, items in menu.items():
        print(f"{category}: {', '.join(items)}")


restaurant_menu = {
    "Starters": ["Soup", "Salad"],
    "Main Course": ["Steak", "Salmon", "Pasta"],
    "Desserts": ["Cake", "Ice Cream"]
}


add_category(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Whiskey")
customer_order = [("Main Course", 1), ("Beverages", 0)] #ordering salmon and cake
order_items = take_order(restaurant_menu, customer_order)
if order_items:
    print("Customer order: ", order_items)
display_menu(restaurant_menu)

#Task 4

def add_room(hotel, room_number):
    if room_number not in hotel:
        hotel[room_number] = True
        print(f"Room {room_number} added")
    else:
        print(f"Room {room_number} already exists")


def is_available(hotel, room_number):
    return hotel.get(room_number, False)

def book_room(hotel, room_number):
    if is_available(hotel, room_number):
        hotel[room_number] = False
        print(f"Room {room_number} booked")
    else:
        print(f"Room {room_number} is not available or does not exist")

def display_rooms(hotel):
    for room, available in hotel.items():
        status = "Available" if available else "Booked"
        print(f"Room {room}: {status}")

hotel_rooms = {"101": True, "102": False, "103":True}


while True:
    print("\nHotel Management System")
    print("1: Add Room\n2: Book Room\n3: Check Room Availability\n4: Display Rooms\n5: Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        room = input("Enter room number to add: ")
        add_room(hotel_rooms, room)
    elif choice == '2':
        room = input("Enter room number to book: ")
        book_room(hotel_rooms, room)
    elif choice == '3':
        room = input("Enter room number to check availability: ")
        available = is_available(hotel_rooms, room)
        print(f"Room {room} is {'available' if available else 'not available'}")
    elif choice == '4':
        display_rooms(hotel_rooms)
    elif choice == '5':
        break
    else:
        print("Invalid choice please try again")

#Task 5

def add_feedback(feedback_dict, sentiment, message):
    feedback_dict.setdefault(sentiment.lower(), []).append(message)
    print(f"Feedback added to {sentiment} category")

def display_feedback_count(feedback_dict):
    for sentiment, messages in feedback_dict.items():
        print(f"{sentiment.title()}: {len(messages)} feedback(s)")

def show_feedback_for_sentiment(feedback_dict, sentiment):
    messages = feedback_dict.get(sentiment.lower(), [])
    if messages:
        print(f"Feedback for '{sentiment}'")
        for message in messages:
            print(f"- {message}")
    else:
        print(f"No feedback available for '{sentiment}'")

customer_feedback = {'positive': [], 'negative': [], 'neutral': []}

add_feedback(customer_feedback, "positive", "Great product")
add_feedback(customer_feedback, 'neutral', "It's ok but it could be better")
add_feedback(customer_feedback, "positive", "Love it")
display_feedback_count(customer_feedback)
show_feedback_for_sentiment(customer_feedback, 'positive')
print(customer_feedback)

#Task 6

def update_inventory(inventory, product, count):
    inventory.update({product:count}) #update function takes key and updates value
    print(f"Inventory updated: {product} - {count} units")

def remove_product(inventory, product):
    if product in inventory:
        removed_count = inventory.pop(product)
        print(f"Product removed: {product} - {removed_count} units were in stock")
    else:
        print("Product not found in inventory")

def display_inventory(inventory):
    print("Current inventory: ")
    for product, count in inventory.items():
        print(f"{product} - {count} units")

store_inventory = {'Laptops': 20, 'Smartphones': 30, 'Headphones': 15}

update_inventory(store_inventory, "Smartphones", 25)
remove_product(store_inventory, 'Laptops')
display_inventory(store_inventory)


#Task 7

import copy

def shallow_copy_schedule(schedules, source_week, target_week):
    schedules[target_week] = schedules[source_week].copy()
    print(f"Week {target_week}'s schedule copied from Week {source_week} (Shallow copy)")


def deep_copy_schedule(schedules, source_week, target_week):
    schedules[target_week] = copy.deepcopy(schedules[source_week])
    print(f"Week {target_week}'s schedule copied from week {source_week} (Deep copy)")

def modify_shift(schedules, week, employee, shift):
    if week in schedules and employee in schedules[week]:
        schedules[week][employee] = shift
        print(f"Shift updated for {employee} in Week {week}: {shift}")
    else:
        print(f"Schedule not found for {employee} in {week}")

def display_schedule(schedules):
    for week, schedule in schedules.items():
        print(f"{week}: ")
        for employee, shift  in schedule.items():
            print(f" {employee}: {shift}")


employee_schedules = {
    "Week 1": {"Alice": "Morning", "Bob": "Evening", "Charlie": "Night"}
}

shallow_copy_schedule(employee_schedules, "Week 1", "Week 2")
deep_copy_schedule(employee_schedules, "Week 1", "Week 3")
modify_shift(employee_schedules, "Week 3", "Alice", "Evening")
display_schedule(employee_schedules)

#Task 8

def add_courses(courses, course_name):
    if course_name not in courses:
        courses[course_name] = {}
        print(f"Course '{course_name}' added")
    else:
        print(f"Course '{course_name}' already exists")


def register_student(courses, course_name, student_name):
    if course_name in courses:
        courses[course_name][student_name] = True
        print(f"Student '{student_name}' registered for {course_name}")
    else:
        print(f"{course_name} does not exist")

def remove_student(courses, course_name, student_name):
    if course_name in courses and student_name in courses[course_name]:
        del courses[course_name][student_name]
        print(f"Student {student_name} removed from {course_name}")
    else:
        print("Student or course not found")

def display_enrollments(courses):
    for course, students in courses.items():
        print(f"Course: {course}")
        for student in students:
            print(f" Student: {student}")



online_courses = {}


add_courses(online_courses, "Python Programming")
add_courses(online_courses, "Data Science")
register_student(online_courses, "Python Programming", "Sam")
register_student(online_courses, "Data Science", "Caden")
remove_student(online_courses, "Data Science", "Caden")
display_enrollments(online_courses)

#Task 9
def add_patient(patients, patient_id, name, age):
    if patient_id not in patients:
        patients[patient_id] = {"name": name, "age": age, "visits": []}
        print(f"Patient '{name}' added with ID: {patient_id}")
    else:
        print(f"Patient with ID {patient_id} already exists")


def display_patient_record(patients, patient_id):
    if patient_id in patients:
        patient = patients[patient_id]
        print(f"Patient ID: {patient_id}\nName: {patient['name']}\nAge: {patient['age']}\nVisits: ")
        for visit in patient["visits"]:
            print(f" Date: {visit['date']}, Notes: {visit['notes']}")
    else:
        print(f"Patient with patient ID {patient_id} not found")

def add_visits(patients, patient_id, date, notes):
    if patient_id in patients:
        patients[patient_id]["visits"].append({"date": date, "notes": notes})
        print(f"Visit on {date} recorded for patient ID: {patient_id}")
    else:
        print(f"Patient with patient ID {patient_id} not found")

clinic_patients = {}

add_patient(clinic_patients, "P001", "Alice Smith", 30)
add_visits(clinic_patients, "P001", "1/2/2024", "Check-up")
add_visits(clinic_patients, "P001", "3/7/2024", "Colonoscopy")
display_patient_record(clinic_patients, "P001")

#Task 10
def add_property(properties, property_id, location, price):
    if property_id not in properties:
        properties[property_id] = {"location": location, "price": price, "status": "available", "inquiries": []}
        print(f"Property ID {property_id} added")
    else:
        print(f"Property ID {property_id} already exists")

def update_status(properties, property_id, status):
    if property_id in properties:
        properties[property_id]["status"] = status
        print(f"Property ID {property_id} status updated to {status}")
    else:
        print("Property ID not found")

def add_inquiry(properties, property_id, customer_name, inquiry):
    if property_id in properties:
        properties[property_id]["inquiries"].append({"customer": customer_name, "inquiry": inquiry})
        print(f"Inquiry added for Property ID {property_id} by {customer_name}")
    else:
        print("Property ID not found")
    
def display_properties(properties):
    for pid, details in properties.items():
        print(f"Property ID: {pid}, Location: {details['location']}, Price: {details['price']}, Status: {details['status']}")
        for inquiry in details["inquiries"]:
            print(f"   Inquiry by {inquiry['customer']}: {inquiry['inquiry']}")
    


real_estate_properties = {}

while True:
    print("\nReal Estate Management System")
    print("1: Add Properties \n2: Update Property Status \n3: Add Inquiry \n4: Display Properties \n5: Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        pid = input("Enter your property ID: ")
        loc = input("Enter location: ")
        price = input("Enter price: ")
        add_property(real_estate_properties, pid, loc, price)
    elif choice == '2': 
        pid = input("Enter your property ID: ")
        status = input("Enter status (available/sold): ")
        update_status(real_estate_properties, pid, status)
    elif choice == '3':
        pid = input("Enter property ID for inquiry: ")
        name = input("Enter customer name: ")
        inquiry = input("Enter inquiry details: ")
        add_inquiry(real_estate_properties, pid, name, inquiry)
    elif choice == '4': 
        display_properties(real_estate_properties)
    elif choice == '5':
        print("Exiting system")
        break
    else:
        print("Invalid choice please try again")