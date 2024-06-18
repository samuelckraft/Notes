import mysql.connector
from mysql.connector import Error

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
    
get_db_connection()