#try/except function

try:
    #code that might cause exception
    user_input = int(input("Enter a valid number: "))
    result = 100/user_input

except ValueError:
    #Code to handle the exception
    print("Oops, that wasn't a number, try again")
except ZeroDivisionError:
    print("Sorry cannot divide by 0")

finally:
    print("this will run no matter what")


#general except block
def perform_complex_calculations(data):
    result = 0
    for item in data:
        result += item **2
    average = result/len(data)
    return average

try:
    data = [1, 2, 'a', 4]
    calculation_results = perform_complex_calculations(data)
except (ValueError, ZeroDivisionError):
    print("Please provide a list of numbers and be sure it's not empty")
except Exception as e:
    print(f"An unexpected error has occured: {e}")

#Raising exceptions
fuel_level = 6
tank_capacity = 5
if fuel_level < 0:
    raise ValueError("Fuel cannot be negative")

class fueltankoverflowerror(Exception):
    """Exception raised when the fuel tank is overfilled"""
    pass

if fuel_level>tank_capacity:
    raise fueltankoverflowerror("Fuel has exceeded the tank capacity")