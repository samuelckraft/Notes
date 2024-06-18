from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
ma = Marshmallow(app)

#schema
class customerschema(ma.Schema):
    name = fields.String(required = True) #fields are like columns on a database; things we need or want to keep track of
    email = fields.String(required = True) #not required unless we do this required=true is there
    phone = fields.String(required = True)
    

    class Meta:
        fields = ('name', 'email', 'phone', 'id')

customer_schema = customerschema()
customers_schema = customerschema(many=True)


def get_db_connection():
    db_name = 'e_commerce_db'

    user = 'root' 

    password = '654U7jsv'

    host = 'localhost'


    try:
        conn = mysql.connector.connect(database = db_name, user = user, password = password, host = host)


        if conn.is_connected(): #checks if its connected
            print('Connected to MySQL successfully')

            return conn
        
    except Error as e:
        print(f'{e}')
        return None
    

@app.route('/')
def home():
    return 'Welcome to the flask music festival'


#after running this below, if I add a /customers at the end of the url it pulls the data from the database
@app.route("/customers", methods = ["GET"]) #method is get/create/delete/update
def get_customers():
    try:
        conn = get_db_connection()

        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500 #error message
        
        cursor = conn.cursor(dictionary=True) #returns rows as dictionaries

        query = "Select * from customers"

        cursor.execute(query)

        customers = cursor.fetchall()

        return customers_schema.jsonify(customers)
    
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


@app.route("/customers", methods = ["POST"])
def add_customer():
    try:
        customer_data = customer_schema.load(request.json)

    except ValidationError as e: #raised if schema isnt met
        print(f"Error: {e}")
        return jsonify(e.messages), 400
    

    try:
        conn = get_db_connection()

        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        cursor = conn.cursor()

        new_customer = (customer_data['name'], customer_data['email'], customer_data['phone'])

        query = "INSERT into customers (name, email, phone) values (%s, %s, %s)"

        cursor.execute(query, new_customer)

        conn.commit()

        return jsonify({"message": "New customer added successfully"}), 201
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"})
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


@app.route("/customers/<int:id>", methods = ["Put"]) #<int:id> is the variable section, allows us to add variables to our url (comprised of converter (int) and variable name (id))
def update_customer(id):
    try:
        customer_data = customer_schema.load(request.json)

    except ValidationError as e: #raised if schema isnt met
        print(f"Error: {e}")
        return jsonify(e.messages), 400
    

    try:
        conn = get_db_connection()

        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        cursor = conn.cursor()

        updated_customer = (customer_data['name'], customer_data['email'], customer_data['phone'], id)

        query = "Update customers set name = %s, email = %s, phone = %s where id = %s"

        cursor.execute(query, updated_customer)

        conn.commit()

        return jsonify({"message": "Updated successfully"}), 201
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"})
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


@app.route("/customers/<int:id>", methods = ["DELETE"]) 
def delete_customer(id):

    try:
        conn = get_db_connection()

        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        cursor = conn.cursor()

        customer_to_remove = (id, )

        cursor.execute("Select * from customers where id = %s", customer_to_remove)

        customer = cursor.fetchone()
        if not customer:
            return jsonify({"Error": "Customer not found"}), 404
        
        query = 'delete from customers where id = %s'

        cursor.execute(query, customer_to_remove)

        conn.commit()

        return jsonify({"message": "Customer removed successfully"}), 201
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"})
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
#one way to run the program (other way is to go in the terminal and type flask run (make sure directory matches))
if __name__ == '__main__':
    app.run(debug=True)

#flask run --debug 
    #will automatically update the website with any changes made to the return function without having to restart the program again