import mysql.connector
from mysql.connector import Error

#Making the connection

    #user and host can be found on mysql under connections

db_name = 'e_commerce_db'

user = 'root' 

password = '654U7jsv'

host = 'localhost'


try:
    conn = mysql.connector.connect(database = db_name, user = user, password = password, host = host)


    if conn.is_connected(): #checks if its connected
        print('Connected to MySQL successfully')
except Error as e:
    print(f'{e}')
finally:
    if conn and conn.is_connected():
        conn.close()
        print('Closed')



#Retrieving data

try:
    conn = mysql.connector.connect(database = db_name, user = user, password = password, host = host)

    cursor = conn.cursor() #creating a cursor to help us communicate with database

    query = "select * from customers" #specific instructions/request

    cursor.execute(query) #asking the cursor to execute the query

    for row in cursor.fetchall(): #fetchall brings the table/column output
        print(row)

except Error as e:
    print(f'{e}')
finally:
    if conn and conn.is_connected():
        cursor.close
        conn.close()



#Adding data
try:
    conn = mysql.connector.connect(database = db_name, user = user, password = password, host = host)

    new_customer = ('John Doe', 'john@example.com', '12346544')

    cursor = conn.cursor()

    query = "insert into customers (name, email, phone) Values (%s, %s, %s)"

    cursor.execute(query, new_customer)

    conn.commit() #finalizes the addition of the new data, ensuring it is recorded and accessible

except Error as e:
    print(f'{e}')
finally:
    if conn and conn.is_connected():
        cursor.close
        conn.close()


#Updating data
if conn is not None:
    try:
        cursor = conn.cursor()

        updated_customer = ('987-654-3210', 5)

        query = 'update customers set phone = %s where id = %s'
        
        cursor.execute(query, updated_customer)

        conn.commit()
        print("Customer details updated successfully")

    finally:
        cursor.close()
        conn.close()


#Removing data
if conn is not None:
    try:
        cursor = conn.cursor()

        customer_to_remove = (7, ) 

        query_check = "Select * from orders where customer_id = %s"

        cursor.execute(query_check, customer_to_remove) #used to troubleshoot and make sure customer can be deleted
        orders = cursor.fetchall()

        if orders:
            print("Cannot delete customer: Customer has associated orders") #can't delete customers if associated with foreign key (i.e. orders)
        else:

            query = 'delete from customers where id = %s'

            cursor.execute(query, customer_to_remove)
            conn.commit()

            print('Customer removed successfully')

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

#adding order
# if conn is not None:
#     try:
#         cursor = conn.cursor()

#         david_id = 4
#         order_date = '2024-01-15'

#         query = "insert into orders (date, customer_id) values (%s, %s)"

#         cursor.execute(query, (order_date, david_id))

#         conn.commit()
#         print('Order added successfully')
        

#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         cursor.close()
#         conn.close()

#updating order
# if conn is not None:
#     try:
#         cursor = conn.cursor()
#         customer_id = 4
#         order_id = 8
#         new_order_date = '2024-04-02'

#         query = 'Update orders set date = %s where id = %s and customer_id = %s'

#         cursor.execute(query, (new_order_date, order_id, customer_id))

#         conn.commit()

#         print('Order updated successfully')
#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         cursor.close()
#         conn.close()

#deleting order
# if conn is not None:
#     try:
#         cursor = conn.cursor()
#         customer_id = 4
#         order_id = 8

#         query = 'delete from orders where id = %s and customer_id = %s'

#         cursor.execute(query, (order_id, customer_id))

#         conn.commit()

#         print('Order deleted successfully')
#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         cursor.close()
#         conn.close()