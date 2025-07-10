#!/usr/bin/env python3
import mysql.connector


host_name = "localhost"
user_name = "root"
user_password = "  "
db_name = "ALX_prodev" 

def stream_users_in_batches(batch_size):
    connection = None
    cursor = None

    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=db_name
    )
    db_cursor = connection.cursor(named_tuple=True)
    query = "SELECT user_id, name, email, age FROM user_data"
    db_cursor.execute(query)
    print("--> Data fetched successfully")
    while True:
        batch = db_cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            #print(user)
            if user.age > 25:
                print(user)
                return user

