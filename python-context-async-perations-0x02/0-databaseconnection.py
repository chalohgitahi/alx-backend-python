#!/usr/bin/env python3

import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        # Initializes the context manager 'with' the database file name.
        self.db_name = db_name
        self.connection = None
    def __enter__(self):
        # Called with the with block
        # This method connects to the database.
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    def __exit__(self):
        # Called when exiting 'with' block
        # Handles commits, rollbacks and connection closing
        if exc_type is None:
            # Error occured inside 'with' block
            self.connection.rollback()
        else:
            # No error occured
            self.connection.commit()
            
        # close the connection
        self.connection.close()
        
        return False
        

with DatabaseConnection('ALX_prodev') as conn:
    cursor = conn.cursor
    
    # Query database
    cursor.execute('SELECT * FROM users')
    
    # Fetch and print the results
    results = cursor.fetchall()
    for user in results:
        print(user)
    
