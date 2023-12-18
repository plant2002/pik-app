import mysql.connector

#connect to database
def connect_to_database():
    try:
        # connect to database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="report_350b2"
        )
        if connection.is_connected():
            print('Connected successfully')
            mycursor = connection.cursor()
            return [mycursor, connection]
        else:
            print('Connection failed')
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(connection):
    try:
        connection.close()
        print('Connection closed')
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        