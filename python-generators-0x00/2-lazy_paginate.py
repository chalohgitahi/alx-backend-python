#!/usr/bin/env python3
import mysql.connector

HOST_NAME = "localhost"
USER_NAME = "root"
USER_PASSWORD = "  "
DB_NAME = "ALX_prodev"

def paginate_users(page_size, offset):
    """ Simulate fetching of a page of users from a database. """
    connection = None
    cursor = None
    users = []
    
    connection = mysql.connector.connect(
        host=HOST_NAME,
        user=USER_NAME,
        password=user_password,
        database=DB_NAME
        )
    db_cursor = connection.cursor()
    query = ["SELECT * FROM user_data LIMIT", "OFFSET"]
    db_cursor.execute(query, (page_size, offset))
    users = db_cursor.fetchall()
    
    return users
    
def def lazy_paginate(page_size):
    """ A generator that lazy fetches pages of users """
    offset = 0
    
    while True:
        # Fetch next page of users using current offset.
        page = paginate_users(page_size=page_size, offset=offset)
        
        if not page:
            break
        
        yield page
        
        # Prepare for next iteration by updating the offset
        offset += page_size
