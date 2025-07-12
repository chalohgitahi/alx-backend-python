#!/usr/bin/env python3
import mysql.connector

# Database connection config
DB_CONFIG = {
    'host': 'localhost',
    'user': 'chaloh',
    'password': '  ',
    'database': 'ALX_prodev'
    }
    

def stream_user_ages():
    connection = None
    cursor = None
    page_size = 3
    offset = 0
    
    connection = mysql.connector.connect(**DB_CONFIG)
    
    while True:
        cursor.connection(dictionary=True)
        query = ["SELECT age FROM user_data LIMIT", "OFFSET"]
        cursor.execute(query, (page_size, offset))
        users = db_cursor.fetchall()
        cursor.close()
        
        if not users:
            break
            
        yield from (user['age'] for user in users)
    
def calculate_average_age(age_generator):
    total_age = 0
    user_count = 0
    
    for age in age_generator:
        """This loop consumes the items from the generator one by one."""
        total_age += age
        user_count += 1
        
    if user_count > 0:
        """calculate avg age."""
        average_age = total_age / user_count
        print(f"Average age of users: {average_age}")
    
   
#if __name__ == "__main__"
    # Create the generator object.
#    age_generator = stream_user_ages()
    
    # Pass the generator to the calculation function to compute the average.
#    calculate_average_age(age_generator)
