#!/usr/bin/env python3
import mysql.connector


host_name = "localhost"
user_name = "root"
user_password = "  "
db_name = "ALX_prodev" 

def stream_users():
    connection = None
    cursor = None

    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=db_name
    )
    db_cursor = connection.cursor()
    print("--> Connection established. Creating a streaming cursor.")
    #db_cursor.execute("SELECT * FROM user_data")
    query = "SELECT user_id, name, email, age FROM user_data"
    db_cursor.execute(query)
    print("--> Data fetched successfully")
    for row in db_cursor:
        yield row

        
stream_users()
